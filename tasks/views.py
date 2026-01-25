from django.shortcuts import render

from.models import Task
from django.http import JsonResponse
from.models import Post, Category, SubCategory
from django.db import connection
from django.contrib.auth.models import User

# Create your views here.
# crud = create, read, update, delete
#NOTE: create equivalent to = Post, read = get, update = put/patch, delete ----> this all are use in rest api's.

def task_list(request):
    tasks = Task.objects.all()
    return render(
        request, 
        "tasks/base.html",
        {"tasks": tasks}
    )


def post_list(request):
    # posts = [
    #     {
    #         'title' : "Educational Content That Adds Value",
    #         'content' : "Educational content forms the foundation of any successful social media strategy. This content type positions your brand as an industry leader while providing genuine value to your audience."
    #     },

    #     {
    #         'title' : "Behind-the-Scenes Content That Humanizes Your Brand",
    #         'content' : "Behind-the-scenes content creates authentic connections between your brand and your audience by showing the human side of your business. In an era where consumers crave authenticity, this content type helps build trust and emotional attachment that purely promotional content cannot achieve."
    #     },

    #     {
    #         'title' : "User-Generated Content for Social Proof",
    #         'content' : "User generated content represents one of the most powerful forms of social proof available to modern brands. When real customers share their experiences with your products or services, it carries far more weight than any branded message you could create."
    #     }
    # ]

    # for post in posts:
    #     Post.objects.create(title=post["title"], content=post["content"], user_id=1)

    data = []
    # # posts = Post.objects.all()     #[NOTE: eikhane "Post" table er jhoto data ache niye direct views e show kre]
    # posts = Post.objects.select_related("user")  #[NOTE: eikhane "select_related" diye database join kre, ar eikhane "user" er sathe eikhane "post" table ta join kra hyeche. ar eikhane shob ta data "posts" namer object tay memory te rakhe then oikhan theke call kre data dekhi. Always eita forward relation(foriegn key, one to one relation) er jonno use kra hoy]
    # #NOTE: N+1 query:
    # for post in posts:
    #     print(post.user.username)
    #     data.append({"title": post.title, "author": post.user.first_name})

    # category = Category.objects.prefetch_related('tasks')
    # print(category)

    task = Task.objects.prefetch_related("subcategory")
    print(task)



   
         

    for query in connection.queries:         #[query check krar jonno ei code lekha hoy]
            print(query, "\n\n")

    return JsonResponse({'status': 'Success', 'result': data})

"""NOTE:
=>select_related use kra hoy: ForeignKey, OneToOne - Forward Relation Access [eikhane ekta query execute hoy, eita jei ekta query kre sheita "join" query]
=>prefetch_related: ManyToMany - Reverse Relation Access [eikhane always duita query execute hoy, ei duitar majhe ekta hoilo "select" query arekta hoilo "in" query]
-----------------------------------------------------------------------------------------------------------------
just Bujhar jonno:
    user: User = User.objects.get(id = 1)     #[NOTE:"user: User" eita ke type hint bole]

    posts = user.post_set.all()
    for post in posts:
        data.append({"title": post.title, "author": post.user.first_name})
"""

