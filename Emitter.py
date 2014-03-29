import gio
import glib
import gobject
import dbus
import dbus.service
import dbus.mainloop.glib

class Emitter(dbus.service.Object):
	
	def __init__(self, conn, object_path='/com/example/TestService/object'):
		dbus.service.Object.__init__(self, conn, object_path)
		
	@dbus.service.signal('com.example.TestService')
	def eventSignal(self, event):
		pass

	@dbus.service.method('com.example.TestService')
	def emitEventSignal(self):
		self.eventSignal("HMM")
		return "Something"

def directory_changed(monitor, file1,file2, event_type):
	if(event_type in (gio.FILE_MONITOR_EVENT_CREATED, \
					gio.FILE_MONITOR_EVENT_DELETED, \
					gio.FILE_MONITOR_EVENT_ATTRIBUTE_CHANGED, \
					gio.FILE_MONITOR_EVENT_MOVED)):
		print event_type


if __name__ == '__main__':		
	
	dbus.mainloop.glib.DBusGMainLoop(set_as_default = True)

	session_bus = dbus.SessionBus()
	name = dbus.service.BusName('com.example.TestService', session_bus)
	object = Emitter(session_bus)
		
	#set up the monitor
	gfile = gio.File(".")
	monitor = gfile.monitor_directory(gio.FILE_MONITOR_NONE, None)
	monitor.connect("changed", directory_changed)

	loop = gobject.MainLoop()
	print "Emmiter is now running"
	loop.run()	
