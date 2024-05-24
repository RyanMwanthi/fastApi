from fastapi import FastAPI,Response ,status , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app= FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating:Optional[int] = None


my_posts = [{"tite":"title post 1", "content":"content post 1", "id":1}, {
    "title":"Favoutote foods","content": "I like burgers","id":2}]  

#For retreiving an individual post 
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p  # return the specific post




@app.get("/")
def read_root():
    return {"Hello": "welcome to my api!!!"}

@app.get("/posts")
def get_posts():
    return{"data":my_posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
# Variable to store the data payload : dictionary = Body 
#TO IMPORT (...)
def create_post(post:Post): # EXTRACT INFORMATION FROM BODY,  
    post_dict=post.dict()                           
    post_dict["id"] = randrange(0,1000000)
    my_posts.append(post_dict) 
    return{"data":post_dict}

@app.get("/posts/{id}")
def get_post(id:int,responce:Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} was not found")
       #responce.status_code = status.HTTP_404_NOT_FOUND
        #return{"message":f"post with id:{id} was not found"}
    print(post)

    return{"personal_details": post}
#title str contnet str Category Bool
