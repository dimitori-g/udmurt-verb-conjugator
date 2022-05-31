import sys

if len(sys.argv) < 2:
	exit('Argument required')

def get_props(verb):
	special_sym = ['д' , 'з', 'л', 'н', 'с', 'т']
	stem, group, pattern_num = ['', 0, 0]
	if verb[-3:] == 'ыны':
		stem = verb[:-3]
		group = 1
		if verb[-4:] == 'ьыны':
			stem = verb[:-4]
			pattern_num = 1
		elif verb[-4:-3] in special_sym:
			pattern_num = 2
	elif verb[-3:] in ['аны', 'яны']:
		stem = verb[:-2]
		group = 2
		pattern_num = 3
	return stem, group, pattern_num

def get_tense_form(tense, stem, pattern_num):
	tense_patterns = {
		'present': [
			['исько', 'иськод', 'е', 'иськом(ы)', 'иськоды', 'о'] ,
			['исько', 'иськод', 'е', 'иськом(ы)', 'иськоды', 'ё'] ,
			['ӥсько', 'ӥськод', 'э', 'ӥськом(ы)', 'ӥськоды', 'о'] ,
			['сько', 'ськод', 'ськоз', 'ськом(ы)', 'ськоды', 'ськозы']
		],
		'past': [
			['и', 'ид', 'из', 'им(ы)', 'иды', 'изы'] ,
			['и', 'ид', 'из', 'им(ы)', 'иды', 'изы'] ,
			['ӥ', 'ӥд', 'ӥз', 'ӥм(ы)', 'ӥды', 'ӥзы'] ,
			['й', 'д', 'з', 'м(ы)', 'ды', 'зы']
		],
		'future': [
			['о', 'од', 'оз', 'ом(ы)', 'оды', 'озы'] ,
			['ё', 'ёд', 'ёз', 'ём(ы)', 'ёды', 'ёзы'] ,
			['о', 'од', 'оз', 'ом(ы)', 'оды', 'озы'] ,
			['ло', 'лод', 'лоз', 'лом(ы)', 'лоды', 'лозы']
		]
	}
	personal_pronounses = ['мон', 'тон', 'со', 'ми', 'тӥ', 'соос']	
	result = []
	for idx, pattern in enumerate(tense_patterns[tense][pattern_num]):
		result.append(personal_pronounses[idx] + ' ' + stem + pattern)
	return result

#----------------------

verb = sys.argv[1]
stem, group, pattern_num = get_props(verb)
if group == 0:
	exit("Given argument isn't udmurt verb")
for tense in ['present', 'past', 'future']:
	print('***' + tense + '***')
	for form in get_tense_form(tense, stem, pattern_num):
		print(form)
	print()