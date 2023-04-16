import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from langchain.llms import OpenAI

@api_view(['POST'])
def get_diet_plan(request):
    name = request.data.get('name')
    age = request.data.get('age')
    weight = request.data.get('weight')
    height = request.data.get('height')
    # Calculate diet plan based on user parameters
    diet_plan = calculate_diet_plan(name, age, weight, height)
    response_data = {'diet_plan': diet_plan}
    return Response(response_data)

def calculate_diet_plan(name, age, weight, height):
    # Calculate diet plan here based on user parameters
    os.environ["OPENAI_API_KEY"] = ""
    llm = OpenAI(model_name="text-davinci-003")
    question = "My name is %(name)s. I am a male of age %(age)s with body weight %(weight)s kgs and %(height)s cm height. \
                I do not have any food allergies. I am from country India. \
                Can you suggest breakfast, lunch, evening snack, dinner diet plan for me?" % \
                {"name": name, "age": age, "weight": weight, "height": height};
    return llm(question)
    # return question
