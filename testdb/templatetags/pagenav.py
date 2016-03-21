from django import template

register = template.Library()

# Usage: {% pagenav students is_paginated paginator %}


@register.inclusion_tag('includes/pagination.html')
def pagenav(object_list, is_paginated, paginator):
	"""Display page navigation for given list of objects"""
	return {
		'object_list': object_list,
		'is_paginated': is_paginated,
		'paginator': paginator
	}

