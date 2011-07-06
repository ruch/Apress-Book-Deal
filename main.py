#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import re
import urllib2
#from google.appengine.ext import urllib2


class MainHandler(webapp.RequestHandler):

  def get(self):
    url='http://www.apress.com/dailydeal'
    #edited on 0703 to update url url='http://apress.com/info/dailydeal'
#   proxies={'http': 'http://www.someproxy.com:3128'}
    #proxies={'http': 'http://localhost:8087'}
    f=urllib2.urlopen(url)
    content=f.read()
    #0703 match=re.search(r'<h3><a href=\'/book/view/([\d]+)\'>(.*)</a></h3>',content)
    match=re.search(r'<title>(.*)</title>',content)
    #match='ruchi'
    if match:
        z="""<html>
            <body>
            <div>
            %s
            <span>
            <b>
            <a href="http://www.apress.com/dailydeal/">%s</a>
            </b>
            </span>
            </div>
            </body>
        </html>
        """%('Today\'s $10 Book is:',match.group(1))
        self.response.out.write(z)
#       self.response.out.write('Today\'s $10 Book is: <br>')
#       self.response.out.write('<b>' match.group(2)'</b>')


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
