import sys
import traceback

import gobject

import dbus
import dbus.mainloop.glib


def emit_signal():
	object.emitEventSignal(dbus_interface="com.example.TestService")
	gobject.timeout_add(2000, loop.quit)
	return False

def event_signal_handler(event_string):
	print ("Event is " + event_string)

def catch_all_events(event_string):
	print ("Received event "+event_string)

if __name__=='__main__':
	dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
	bus = dbus.SessionBus()

	try:
		object = bus.get_object("com.example.TestService", "/com/example/TestService/object")
		object.connect_to_signal("eventSignal", event_signal_handler, dbus_interface="com.example.TestService")

	except dbus.DBusException:
		traceback.print_exc()
		sys.exit(1)

	bus.add_signal_receiver(catch_all_events, dbus_interface = "com.example.TestServices", signal_name = "eventSignal")

	gobject.timeout_add(2000, emit_signal)
	loop = gobject.MainLoop()
	loop.run()
