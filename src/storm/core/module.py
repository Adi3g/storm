
class ModuleBase():
    def __init__(self, controllers=[], providers=[], imports=[], middleware=[], module_cls=None):
        """
        Initialize the module with controllers, providers, imports, and middleware.
        :param controllers: List of controller classes.
        :param providers: List of provider (service) classes.
        :param imports: List of other modules to be imported.
        :param middleware: List of middleware classes.
        """
        self.controllers = controllers
        self.providers = providers
        self.imports = imports
        self.middleware = middleware
        self._module_cls = module_cls
        
        if hasattr(module_cls, 'onInit') and callable(module_cls.onInit):
            module_cls.onInit(self)
            self.onInit()
       
        if hasattr(module_cls, 'onDestroy') and callable(module_cls.onDestroy):
            module_cls.onDestroy(self)

    def register(self, container):
        """
        Register all providers, controllers, and middleware in the container.
        :param container: The DI container.
        """
        # Register imported modules first
        for imported_module in self.imports:
            imported_module.register(container)

        # Register providers
        for provider in self.providers:
            name = provider.__name__
            container.register(name, provider, singleton=getattr(provider, '__singleton__', True))

        # Register controllers with middleware
        for controller in self.controllers:
            name = controller.__name__
            container.register(name, controller, singleton=True)

        # Register middleware
        for middleware in self.middleware:
            container.register(middleware.__name__, middleware, singleton=True)

    def onInit(self):
        """
        Hook for module initialization.
        """
        pass
    
    def onDestroy(self):
        """
        Hook for module destruction.
        """
        pass

    def on_bootstrap(self):
        """
        Called after all modules are loaded and the app is ready to run.
        """
        pass

    def on_shutdown(self):
        """
        Called when the application is shutting down.
        """
        pass