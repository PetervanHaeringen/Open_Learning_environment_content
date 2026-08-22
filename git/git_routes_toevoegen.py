# ======================================================================================================
#  GIT — content routes (YAML + Markdown systeem)
#  Voeg deze routes toe aan instructions/routes.py
#  ter vervanging van de hardcoded git_module1 t/m git_module4 routes
# ======================================================================================================

@instructions_bp.route("/git/content/overview")
@login_required
def git_content_overview():
    modules = load_track_modules("git")
    return render_template(
        "git/content_overview.html",
        modules=modules
    )


@instructions_bp.route("/git/content/<module_name>")
@login_required
def git_content_module(module_name):
    lesson = load_lesson("git", module_name)

    if not lesson:
        abort(404)

    html_content = markdown.markdown(
        lesson["content"],
        extensions=["extra"]
    )

    user_id = session["user_id"]
    answer_map = get_answer_map(user_id, lesson["module_slug"])

    return render_template(
        "git/content_lesson.html",
        lesson=lesson,
        html_content=html_content,
        answer_map=answer_map
    )


@instructions_bp.route("/submit-git-answer", methods=["POST"])
@login_required
def submit_git_answer():
    module_slug = request.form.get("module_slug")
    module_folder = request.form.get("module_folder")
    question_id = request.form.get("question_id")
    user_answer = request.form.get(question_id)

    lesson = load_lesson("git", module_folder)

    if not lesson:
        abort(404)

    question = next(
        (q for q in lesson["questions"] if q["id"] == question_id),
        None
    )

    if not question:
        abort(404)

    user_id = session["user_id"]

    if question.get("type") == "open":
        upsert_answer(
            user_id=user_id,
            module_slug=module_slug,
            question_id=question_id,
            user_answer=user_answer,
            is_correct=False
        )
        return redirect(
            url_for("instructions.git_content_module", module_name=module_folder)
            + f"#{question_id}"
        )

    is_correct = check_answer(question, user_answer)
    upsert_answer(
        user_id=user_id,
        module_slug=module_slug,
        question_id=question_id,
        user_answer=user_answer,
        is_correct=is_correct
    )

    return redirect(
        url_for("instructions.git_content_module", module_name=module_folder)
        + f"#{question_id}"
    )
