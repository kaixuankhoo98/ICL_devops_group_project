#from os import sendfile
from asyncio import subprocess
from flask import Blueprint, request, render_template, flash, send_file
from literature_searcher import query_processor
import subprocess
import os

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
    elif format == "markdown":
        # need to generate a markdown file, save to disk, send to client by putting in filename for this function
        search_results = query_processor.process(query)
        file = open( "/root/literature_searcher/markdown_query.md", "w")        
        # need to save write to makedown_query.md
        file.write(str(search_results))
        file.close()
        return send_file("/root/literature_searcher/markdown_query.md", mimetype = "markdown", as_attachment=True)
    #if pdf download request
    else:
        search_results = query_processor.process(query)
        file = open( "/root/literature_searcher/markdown_query2.md", "w")
        #pandoc does not like newline char, need to write line by line
        for l in search_results:
            file.write(l)

        #pandoc arguments. relative paths not working. need to adjust when adding to docker.
        #args = [
         #   "pandoc",
          #  "markdown_query.md",
           # "-s",
            #"-o",
            #"pdf_query.pdf"
            #]
        #execute pandoc as a subprocess.
        #result = subprocess.Popen(args, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #print error log
        #stdout, stderr = result.communicate()
        #print("pandoc stderr: " + str(stderr))

        cmd = ["pandoc", "-s", "/root/literature_searcher/markdown_query2.md", "-o", "/root/literature_searcher/pdf_query.pdf"]
        subprocess.run(cmd)

        for f in os.listdir("/root/literature_searcher"):
            file.write(f)
        
        file.close()

        return send_file("/root/literature_searcher/markdown_query2.md", mimetype = "markdown", as_attachment=True)
        return send_file("/root/literature_searcher/pdf_query.pdf", mimetype = "application/pdf", as_attachment=True)

@bp.route("/markdown_result_page.md")
def generate_large_csv():
    def generate():
        for row in iter_all_rows():
            yield f"{','.join(row)}\n"
    return app.response_class(generate(), mimetype='text/csv')
