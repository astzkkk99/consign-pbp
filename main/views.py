from django.shortcuts import render

def show_main(request):
    context = {
        'title' : "CONSIGN!",
        'item_type' : 'Console',
        'item_name' : 'PS4',
        'item_price': '2000000',
        'item_description': 'PS4 bekas, udah dipake 4 tahun, minus lecet aja'
    }

    return render(request, "main.html", context)
