from flask import Blueprint, request, render_template, flash, send_file
from literature_searcher import query_processor

bp = Blueprint("search_result", __name__)

@bp.route("/search_result", methods=["GET", "POST"])
def response():

    query = request.args["search_query"]
    if not query:
        flash("No query")
    format = request.args["output_format"]
    if format == "html":
        search_results = query_processor.process(query)
        return render_template("search_result.html", search_results=search_results)
    # If file is markdown
    else:
        # need to generate a markdown file, save to disk, send to client by putting in filename for this function
        search_results = query_processor.process(query)
        file = open( "/tmp/markdown_query.md", "w")
        # need to save write to makedown_query.md
        file.write(str(search_results))
        file.close()
        return send_file("/tmp/markdown_query.md", mimetype = "markdown", as_attachment=True)

@bp.route("/markdown_result_page.md")
def generate_large_csv():
    def generate():
        for row in iter_all_rows():
            yield f"{','.join(row)}\n"
    return app.response_class(generate(), mimetype='text/csv')