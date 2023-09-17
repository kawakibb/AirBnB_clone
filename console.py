def do_create(self, arg):
    """Create a new instance of BaseModel, User, etc."""
    args = arg.split()
    if len(args) == 0:
        print("** class name missing **")
        return

    class_name = args[0]
    if class_name not in class_names:
        print("** class doesn't exist **")
        return

    if len(args) < 2:
        print("** instance id missing **")
        return

    new_instance = eval(f'{class_name}()')
    new_instance.id = args[1]
    for pair in args[2:]:
        key, value = pair.split('=')
        setattr(new_instance, key, value)
    new_instance.save()
    print(new_instance.id)

def do_show(self, arg):
    """Prints the string representation of
    an instance based on the class name and id."""
    args = arg.split()
    if len(args) == 0:
        print("** class name missing **")
        return
    class_name = args[0]
    if class_name not in class_names:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = args[0] + "." + args[1]
    objects = storage.all()
    if key in objects:
        print(objects[key])
    else:
        print("** no instance found **")

def do_destroy(self, arg):
    """Deletes an instance based on the class name and id."""
    args = arg.split()
    if len(args) == 0:
        print("** class name missing **")
        return
    class_name = args[0]
    if class_name not in class_names:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = args[0] + "." + args[1]
    objects = storage.all()
    if key in objects:
        del objects[key]
        storage.save()
    else:
        print("** no instance found **")

def do_update(self, arg):
    """Updates an instance based on the class name
    and id by adding or updating attribute."""
    args = arg.split()
    if len(args) == 0:
        print("** class name missing **")
        return
    class_name = args[0]
    if class_name not in class_names:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = args[0] + "." + args[1]
    objects = storage.all()
    if key not in objects:
        print("** no instance found **")
        return
    if len(args) < 3:
        print("** attribute name missing **")
        return
    if len(args) < 4:
        print("** value missing **")
        return
    attribute_name = args[2]
    attribute_value = args[3]
    setattr(objects[key], attribute_name, attribute_value)
    storage.save()

def do_all(self, arg):
    """Prints all string representations of
    all instances based or not on the class name."""
    args = arg.split()
    objects = storage.all()
    if len(args) == 0:
        print([str(obj) for obj in objects.values()])
    else:
        class_name = args[0]
        if class_name not in class_names:
            print("** class doesn't exist **")
            return
        filtered_objects = [str(obj) for key, obj in objects.items() if key.startswith(class_name + ".")]
        print(filtered_objects)
