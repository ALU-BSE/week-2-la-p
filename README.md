### Django Pagination Project

A Django web application that demonstrates efficient pagination for displaying book records. This project was created as part of a hands-on group activity to learn about Django's pagination capabilities.

## 📚 Project Overview

This application displays a collection of books with pagination controls, allowing users to navigate through the book collection efficiently. It demonstrates how to handle large datasets in Django by displaying them in smaller, more manageable chunks.

## 🔑 Admin Access

The project includes an admin interface to manage book records:

- **URL**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Username**: admin
- **Password**: 123admin123


## 🚀 Installation and Setup

### Prerequisites

- Python 3.x
- Django


### Installation Steps

1. **Clone the repository**

```shellscript
git clone https://github.com/yourusername/pagination-project.git
cd pagination-project
```


2. **Create a virtual environment** (optional but recommended)

```shellscript
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


3. **Install Django**

```shellscript
pip install django
```


4. **Apply migrations**

```shellscript
python manage.py makemigrations
python manage.py migrate
```


5. **Load sample data**

```shellscript
python manage.py loaddata books.json
```


6. **Create a superuser** (for admin access)

```shellscript
python manage.py createsuperuser
# Use admin/123admin123 as credentials
```


7. **Run the development server**

```shellscript
python manage.py runserver
```


8. **Access the application**

1. Main application: [http://127.0.0.1:8000/books/](http://127.0.0.1:8000/books/)
2. Admin interface: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)





## 📁 Project Structure

```plaintext
pagination_project/
├── books/                      # Main application
│   ├── fixtures/               # Sample data
│   │   └── books.json          # Book records in JSON format
│   ├── migrations/             # Database migrations
│   ├── templates/              # HTML templates
│   │   └── books/
│   │       ├── base.html       # Base template with styling
│   │       └── book_list.html  # Book listing with pagination
│   ├── admin.py                # Admin configuration
│   ├── apps.py                 # App configuration
│   ├── models.py               # Book model definition
│   ├── tests.py                # Test cases
│   ├── urls.py                 # URL routing for books app
│   └── views.py                # View functions
├── pagination_project/         # Project settings
│   ├── asgi.py
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL routing
│   └── wsgi.py
└── manage.py                   # Django management script
```

## 📖 Usage

### Viewing Books

1. Navigate to [http://127.0.0.1:8000/books/](http://127.0.0.1:8000/books/)
2. Browse through the paginated book list
3. Use the pagination controls at the bottom to navigate between pages
4. Change the number of items per page using the dropdown menu (if implemented)


### Managing Books (Admin)

1. Navigate to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
2. Log in with admin/123admin123
3. Click on "Books" under the "BOOKS" section
4. Add, edit, or delete book records


## 🔍 Implemented Features

- Basic pagination with navigation controls
- Admin interface for managing books
- Dynamic items per page selection (bonus challenge)
- Clean, responsive UI


---

# Original Assignment Instructions

## **Django Pagination Hands-On Group Activity**

**Objective:** Create a Django project, populate a model with AI-generated data, and implement pagination to display records efficiently.

## **Activity Overview**

- **Duration:** 30 minutes
- **Group Size:** 4-6 learners per group
- **Prerequisites:** Basic Python knowledge, Django installed (`pip install django`)
- **Tools Needed:** Python, Django, Browser, AI Tool (e.g., ChatGPT, Mockaroo)


## **Step-by-Step Instructions**

### **1. Create a New Django Project**

**Guidelines:**

1. Open a terminal and run:

```shellscript
django-admin startproject pagination_project
cd pagination_project
python manage.py startapp books
```


2. Add `'books'` to `INSTALLED_APPS` in `settings.py`.
3. Run migrations:

```shellscript
python manage.py migrate
```




### **2. Define a Single Model**

**Task:** Create a `Book` model with fields:

- `title` (CharField)
- `author` (CharField)
- `published_year` (IntegerField)


```python
# books/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title
```

- Register the model in `admin.py`:

```python
from django.contrib import admin
from .models import Book
admin.site.register(Book)
```


- Run:

```shellscript
python manage.py makemigrations
python manage.py migrate
```




### **3. Populate the Model with AI-Generated Data**

**Option 1: Use ChatGPT**

- Prompt: *"Generate 50 fake book records in JSON format with title, author, and published_year."*
- Save the output as `books.json` in a `fixtures` folder.
- Load data:

```shellscript
python manage.py loaddata books.json
```




**Option 2: Use Mockaroo**

- Visit [Mockaroo](https://www.mockaroo.com/) and configure fields:

- `title` (Book Title)
- `author` (Full Name)
- `published_year` (Number, 1900-2023)



- Download as JSON and load as above.


### **4. Implement Pagination**

#### **Step 1: Create a View**

```python
# books/views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all().order_by('title')
    paginator = Paginator(books, 5)  # 5 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'page_obj': page_obj})
```

#### **Step 2: Add URL**

```python
# pagination_project/urls.py
from django.contrib import admin
from django.urls import path
from books.views import book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list, name='book_list'),
]
```

#### **Step 3: Create a Template**

```html
<!-- books/templates/books/book_list.html -->
<h1>Book List</h1>
<ul>
  {% for book in page_obj %}
    <li>{{ book.title }} ({{ book.published_year }}) by {{ book.author }}</li>
  {% endfor %}
</ul>

<div class="pagination">
  <span class="step-links">
    {% if page_obj.has_previous %}
      <a href="?page=1">&laquo; first</a>
      <a href="?page={{ page_obj.previous_page_number }}">previous</a>
    {% endif %}

    <span class="current">
      Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
    </span>

    {% if page_obj.has_next %}
      <a href="?page={{ page_obj.next_page_number }}">next</a>
      <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
    {% endif %}
  </span>
</div>
```

### **5. Test & Discuss**

- Run the server:

```shellscript
python manage.py runserver
```


- Visit `http://127.0.0.1:8000/books/` and navigate pages.
- **Discussion Questions:**

- Why is pagination important for large datasets?
- How would you customize items per page dynamically?
- What happens if `page` is invalid?





## **Bonus Challenges**

**Dynamic Items Per Page:** Add a dropdown to change `per_page` value.**Styled Pagination:** Use Bootstrap for better UI.**Search + Pagination:** Filter books by author/year before paginating.

## **Conclusion**

Learners will:

- Set up a Django project from scratch.
- Populate a model using AI tools.
- Implement and customize pagination.


**Happy Coding!**