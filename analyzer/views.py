from django.shortcuts import render
import pandas as pd

def Home_Page(request):
    return render(request, 'home.html')

def Upload(request):
    if request.method == "POST":
        file = request.FILES["file"]

        # read dataset
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return render(request, "upload.html", {"error": "Unsupported file type"})

        # dataset preview
        data_preview = df.head().to_html()

        context = {
            "preview": data_preview,
            "rows": df.shape[0],
            "cols": df.shape[1],
            "columns": df.columns.tolist()
        }

        return render(request, "results.html", context)

    return render(request, "upload.html")

def Result(request):
    return render(request, 'results.html')

def Insights(request):
    return render(request, 'insights.html')
