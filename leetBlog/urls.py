from django.urls import path
from .views import Home,PostView,AddPost,UpdatePost,DeletePost,AddComment
urlpatterns = [
    
    path('' ,Home.as_view() ,name ='home' ),
    path('post/<int:pk>' ,PostView.as_view() ,name ='post' ),
     path('add/' ,AddPost.as_view() ,name ='add' ),
      path('update/<int:pk>' ,UpdatePost.as_view() ,name ='update'),
      path('delete/<int:pk>' ,DeletePost.as_view() ,name ='delete'),
      path('post/<int:pk>/comments' ,AddComment.as_view() ,name ='comment'),

      

     


]