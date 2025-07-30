def make_car(manu, model, **attributes):

	car = {}

	car['manufacturer'] = manu

	car['model'] = model

	for key, value in attributes.items():

		car[key] = value

	return car
	
finished_car = make_car('Chrysler', '200', color='white', engine='v6')
print(finished_car)
