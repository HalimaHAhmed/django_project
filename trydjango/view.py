from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string


def home(request):
    # name = 'halima'
    random_id = random.randint(1, 4)

    # from databases
    article_obj = Article.objects.get(id=random_id)

    my_list = [102, 13, 342, 1331, 213]
    my_list_str = ""
    for x in my_list:
        my_list_str += f"number is{x}\n"
    # article_title = article_obj.title
    # article_content = article_obj.content
    context = {
        "my_list_str": my_list_str,
        "title": article_obj.title,
        "id":  article_obj.id,
        "content": article_obj.content



    }

    # html_string = f"""

    # <h1>{article_title} ({article_obj.id})!</h1>
    # """

    # p_string = f"""

    # <p>{article_content}!</p>
    # """
    # from django template
    # tmpl = get_template("home.html")
    # tmp_string = tmpl.render(context=context)

    html_string = render_to_string("home.html", context=context)
    html_string = render_to_string("base.html", context=context)
    # html_string = """
    # <h1>{title} (id:{id}!)</h1>
    # <p>{content}!</p>
    # """.format(**context)

    return HttpResponse(html_string)

# this is testing
