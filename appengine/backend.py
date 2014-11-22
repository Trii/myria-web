from abc import abstractmethod, ABCMeta


class Backend(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def catalog(self):
        """Returns an instance of the catalog to use for dataset checking"""

    @abstractmethod
    def algebra(self):
        """Returns corresponding target algebra"""

    @abstractmethod
    def connection(self):
        """Returns an instance of a connection"""

    @abstractmethod
    def compile_query(self, query, logical_plan, physical_plan, language=None):
        """Takes the raw query, logical,b and physical plan
           Returns JSON of compiled query"""

    @abstractmethod
    def execute_query(self, logical_plan, physical_plan, language=None,
                      profile=False):
        """Executes the query, using raw query, logical, and physical plans
           returns the status and corresponding url"""

    @abstractmethod
    def get_query_status(self, query_id):
        """Returns the query status of query_id"""

    @abstractmethod
    def connection_string(self):
        """Returns the status of the connection of the backend"""

    @abstractmethod
    def backend_url(self):
        """Returns the url for more information about the backend project"""

    @abstractmethod
    def num_queries(self, limit, max_):
        """Returns the total number of queries for the backend"""

    def connection_url(self, uri_scheme="http"):
        return "{s}://{h}:{p}".format(s=uri_scheme,
                                      h=self.hostname, p=self.port)