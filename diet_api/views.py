import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from langchain.llms import OpenAI
from .models import DietPlannerSetting

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
    os.environ["OPENAI_API_KEY"] = DietPlannerSetting.objects.first().openai_api_key
    llm = OpenAI(model_name=DietPlannerSetting.objects.first().openai_model_name)
    question = DietPlannerSetting.objects.first().prompt % \
                {"name": name, "age": age, "weight": weight, "height": height};
    print(os.environ["OPENAI_API_KEY"])
    print(DietPlannerSetting.objects.first().openai_model_name)
    print(question)
    return llm(question)
    # return question
