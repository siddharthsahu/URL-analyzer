from urlparse import urlparse


class Analyzer:
    """class to perform the url analysis"""

    def __init__(self, url):
        self.url = url
        self.parsed_url = urlparse(url)

    def print_intro(self):
        print "Analysis of URL: " + self.url + "\n"
        print "------------------------------------------------------------------------------------------\n"

    def analyze_protocol(self):
        if self.parsed_url.scheme is None:
            print "Protocol: No protocol is specified in given URL"
            return

        # python doesn't have switch statement. This is standard way to implement switch behavior
        switcher = {
            'http': "Protocol: This is HTTP",
            'https': "Protocol: This is HTTPS",
            'ftp': "Protocol: This is FTP"
        }
        print switcher.get(self.parsed_url.scheme, "Protocol: Given protocol is not recognized")

    def analyze_domain(self):
        if self.parsed_url.netloc is None:
            print "Domain: Unable to identify domain name"
        print "Domain: " + self.parsed_url.netloc

    def analyze_path(self):
        if self.parsed_url.path is None or self.parsed_url.path == "":
            print "Request path: No path is present in given URL"
        else:
            print "Request path: " + self.parsed_url.path

    def analyze_port(self):
        if self.parsed_url.port is None:
            print "Port: No port is provided in given URL"
        else:
            print "Port: " + self.parsed_url.port

    def analyze_query(self):
        if self.parsed_url.query is None or self.parsed_url.query == "":
            print "Query Arguments: No query arguments is provided in given URL"
        else:
            print "Query Arguments: " + self.parsed_url.query


    def perform_analysis(self):
        self.print_intro()
        self.analyze_protocol()
        self.analyze_domain()
        self.analyze_path()
        self.analyze_port()
        self.analyze_query()


class UserInterface:
    """class to interact with user and drive the program"""

    def __init__(self):
        pass

    def serveUser(self):
        url = raw_input("\nPlease enter URL string:").strip()
        analyzer = Analyzer(url)
        analyzer.perform_analysis()


user_interface = UserInterface()
user_interface.serveUser()
