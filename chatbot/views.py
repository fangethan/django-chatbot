from chatbot.api_key_holder import get_openai_api_key
from django.shortcuts import render
from django.http import JsonResponse
import openai

# This is where you create your own api key and create a new file to store it
# Make sure the file holding the api key is ignored to protect the api key from being insecure
openai_api_key = get_openai_api_key()
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message, 
        max_tokens = 150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer

# Create your views here.
def chatbot(request):
    if request.method == "POST":
        message = request.POST.get("message")
        response = ask_openai(message)
        return JsonResponse({"message": message, "response": response})

    return render(request, "chatbot.html")
