from curtsies import Input


def get_input_character():
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
        	return e
        
def check_if_key_is_pressed(key):
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			if e == key:
				print("You are pressing the right key")
			else:
				print("You are pressing the WRONG key")

def main():
	print("Press the key:")
	pressed_character = get_input_character()
	print(f"Your key is: {pressed_character}")
	check_if_key_is_pressed(pressed_character)

if __name__ == '__main__':
    print("Main function is running")
    main()