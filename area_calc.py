print("Wellcome to small calculator of the area of triangle/paralellogram usign 3 coordinates on the plane");
shape = input("to continue, choose a shape: triangle / quadrilateral: ");

coords = {
	'coord_1': [],
	'coord_2': [],
	'coord_3': [],
	'coord_4': [],
}

if shape == 'triangle':
	def CoordAssigner(coord1, coord2, variable):
		coords[variable].append(coord1);
		coords[variable].append(coord2);



	for i in range(3):
		point = i + 1
		input_coordinate_X = float(input(f'Write "X" coordinate of point {point}: '));
		input_coordinate_Y = float(input(f'Write "Y" coordinate of point {point}: '));
		CoordAssigner(input_coordinate_X, input_coordinate_Y , f'coord_{point}');

	def CalcArea(coord1, coord2, coord3):
		area = abs((coord1[0] * coord2[1] + coord2[0] * coord3[1] + coord3[0] * coord1[1]) - (coord1[1] * coord2[0] + coord2[1] * coord3[0] + coord3[1] * coord1[0]))/2
		return area

	print(CalcArea(coords['coord_1'],coords['coord_2'],coords['coord_3']));

elif shape == 'paralellogram':
	def CoordAssigner(coord1, coord2, variable):
		coords[variable].append(coord1);
		coords[variable].append(coord2);

	for i in range(4):
		point = i + 1
		input_coordinate_X = float(input(f'Write "X" coordinate of point {point}: '));
		input_coordinate_Y = float(input(f'Write "Y" coordinate of point {point}: '));
		CoordAssigner(input_coordinate_X, input_coordinate_Y , f'coord_{point}');

	def CalcArea(coord1, coord2, coord3, coord4):
		area = abs(
    			coord1[0] * coord2[1] +
    			coord2[0] * coord3[1] +
    			coord3[0] * coord4[1] +
    			coord4[0] * coord1[1] -
    			coord1[1] * coord2[0] -
    			coord2[1] * coord3[0] -
    			coord3[1] * coord4[0] -
    			coord4[1] * coord1[0]
		) / 2

		return area

	print(CalcArea(coords['coord_1'],coords['coord_2'],coords['coord_3'], coords['coord_4']));
else: 
	print('Choose triangle or quadrilateral')
