#Implement HTML to prepare scraper output for display on frontend.
def pretty_print(contents: dict) -> str:
  out = "<html>"
  out += """<style>
* {
	font-family: verdana;
}
</style>""" #font

  out += "<p>"
  for k in contents.keys():
   v = contents[k]
   out += f"{k}: {v}<br>"
  out += "</p>"

  out += "</html>"
  return out