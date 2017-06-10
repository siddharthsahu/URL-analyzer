from urlparse import urlparse
import socket
import subprocess


class Analyzer:
    """class to perform the url analysis"""

    def __init__(self, url):
        self.url = url
        self.parsed_url = urlparse(url)
        if self.parsed_url.netloc is not None or self.parsed_url.netloc != "":
            self.ip_add = socket.gethostbyname(self.parsed_url.netloc)
        else:
            self.ip_add = None

    def get_ip_add(self):
        if self.ip_add is not None:
            print "IP Address: " + self.ip_add
        else:
            print "IP Address: Unable to resolve IP address"

    def print_intro(self):
        print "Analysis of URL: " + self.url + "\n"
        print "------------------------------------------------------------------------------------------\n"

    def analyze_protocol(self):
        if self.parsed_url.scheme is None:
            print "Protocol: No protocol is specified in given URL"
            return

        # python doesn't have switch statement. This is standard way to implement switch behavior
        switcher = {
            'http': "Protocol: HTTP",
            'https': "Protocol: HTTPS",
            'ftp': "Protocol: FTP"
        }
        print switcher.get(self.parsed_url.scheme, "Protocol: Given protocol is not recognized")

    def analyze_domain(self):
        if self.parsed_url.netloc is None:
            print "Domain: Unable to identify domain name"
        print "Domain: " + self.parsed_url.netloc

    def analyse_site_status(self):
        ping_output = subprocess.check_output(["ping", "-c1", self.parsed_url.netloc])
        if "unknown host" in ping_output:
            print "Page status: Unable to resolve domain"
        elif "1 received" in ping_output:
            print "Page status: Page is up and running"
        else:
            print "Page status: Page is down"


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

    def obtain_whois_info(self):
        if self.parsed_url.netloc is None:
            print "Whois information: Unable to retrieve information"
        whois_output = subprocess.check_output(["whois", self.parsed_url.netloc.split(".")[1]])
        print "Whois information: " + whois_output

    def perform_analysis(self):
        self.print_intro()
        self.analyze_protocol()
        self.analyze_domain()
        self.analyse_site_status()
        self.get_ip_add()
        self.analyze_path()
        self.analyze_port()
        self.analyze_query()
        self.obtain_whois_info()


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
