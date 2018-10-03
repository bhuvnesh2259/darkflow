template = '''<annotation>
	<folder>VOC2007</folder>
	<filename>{filename}</filename>
	<source>
		<database>OpenImagese</database>
		<annotation></annotation>
		<image></image>
		<flickrid></flickrid>
	</source>
	<owner>
		<flickrid></flickrid>
		<name></name>
	</owner>
	<size>
		<width>{width}</width>
		<height>{height}</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
{objectstr}
</annotation>'''


bbox = '''<object>
		<name>{label}</name>
		<truncated>{truncated}</truncated>
		<bndbox>
			<xmin>{xmin}</xmin>
			<ymin>{ymin}</ymin>
			<xmax>{xmax}</xmax>
			<ymax>{ymax}</ymax>
		</bndbox>
	</object>
'''
