from scraper.models import Course


def filter_cs(cs):
  #quick edit to see what we get from the request - Sophie

  out = ""
  crs_list: list[Course] = []

  class_data = dict(dict()) #main body of data passed that will be used to organize inputs into out str
  cur_section = ""
  num_sections = ""
  class_name = ""
  #for line in cs.split(","): 
  lines = cs.split(",")
  i = 0
  while i < len(lines):
      line = lines[i]
      #filter for data for database fields. will be put into database code when that's written.
      fields_we_want = ["sectionComponentClass", "classNbr"] 
      if any([field in line for field in fields_we_want]):
          #if any of the fields appear in the current line
          if "rows" in line and "classNbr" in line:
              a = line.rindex(":")
              cur_section = "".join([c for c in line[a:] if c.isnumeric()])
              class_data[cur_section] = dict() #populate with fields as we find them

              while "daysTimes" not in line: #beginning of section to parse
                  i += 1
                  line = lines[i]
              while "acadCalendar" not in line: #end of section to parse
                  idx = line.index(":")
                  k = line[:idx].strip('"')
                  v = line[idx:].strip('"')
                  class_data[cur_section][k] = v
                  i += 1
                  line = lines[i]

      if "numSectionsFound" in line: num_sections = line[line.rindex(":") + 1:].strip('"')
      if '"classes":[{"title":' in line: class_name = line[line.rindex(":") + 1:].strip('"')
      i += 1

  out += num_sections + " for " + class_name + "<br><br>"
  #class_data["class_name"] = class_name
  for section in class_data.keys():
      out += "section: " + section + "<br>"
      for k in class_data[section].keys():
        dat = class_data[section][k]

        out += f"{k} {dat}" + "<br>"
      out += "<br>"

      sec = class_data[section]
    #   crs = Course(
    #         section_id  = section,
    #         #class_name  = class_data["class_name"],
    #         instructors = sec["instructor:"],
    #         days_week = sec["statEndDate:"],
    #     ) # does this work?
    #   crs_list.append(crs)
  print(out)
  out = out.replace("\n", "<br>")


  return [out, class_data, crs_list]

#ret = [formatted_str, dictionary, course_object]