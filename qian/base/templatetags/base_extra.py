from django.template import Library

register = Library()

@register.filter
def as_range(value):
    """
    Filter - returns a list containing range made from given value
    
    Usage (in template):
    <ul>
      {% for i in 3|as_range %}
        <li>{{ i }}. Do something.</li>
      {% endfor %}
    </ul>
    
    Result with HTML:
    <ul>
      <li>0. Do something.</li>
      <li>1. Do something.</li>
      <li>2. Do something.</li>
    </ul>
    
    Instead of 3 one may use the variable set in the views.
    """
    return range(value)
