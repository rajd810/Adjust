import datetime
from django.db.models import Sum

def str_to_datetime(date_str, format = '%d.%m.%Y'):
	try:
		date_obj = datetime.datetime.strptime(date_str, format)
		return date_obj.date()
	except:
		return None


def get_date_filter(date_str, date_lte, date_gte, date_from, date_to, month, year):
	date_filter = {}
	
	if date_str:
		
		date_obj = str_to_datetime(date_str)
		if date_obj:
			date_filter = {
				'date__year': date_obj.year,
				'date__month': date_obj.month,
			}
			if date_obj.day:
				date_filter.update({
					'date__day': date_obj.day
				})

	elif date_lte:
		date_obj = str_to_datetime(date_lte)
		if date_obj:
			date_filter = {
				"date__lte": date_obj
			}
	elif date_gte:
		date_obj = str_to_datetime(date_gte)
		if date_obj:
			date_filter = {
				"date__gte": date_obj
			}
	elif date_from and date_to:
		date_from_obj = str_to_datetime(date_from)
		date_to_obj = str_to_datetime(date_to)
		if date_from_obj and date_to_obj:
			date_filter = {
				'date__gte': date_from_obj,
				'date__lte': date_to_obj
			}
	elif month and year:
		date_filter = {
			'date__year': year,
			'date__month': month
		}
	elif year:
		date_filter = {
			'date__year': year,
		}
	return date_filter

def add_other_filters(_filter, channel, country, os):
 
	if channel:
		_filter.update({
			'channel': channel
		})
	if country:
		_filter.update({
			'country': country
		})
	if os:
		_filter.update({
			'os': os
		})

def get_sum_annotation(aggregate_sum_list, only_aggregate=False):
	sum_annotation = {}
	for key in aggregate_sum_list:
		sum_annotation.update({
			key + '_sum' if only_aggregate else key: Sum(key),
		})
	return sum_annotation