a = """<select name="subj_code" style="width:350px" size="18" onchange="subj_select(this.form,this.options[this.selectedIndex].value);">
<option></option>
<option value="">-----Unrestricted Electives in Social Sciences-----</option>
<option value="HN9010">HN9010 - Spore: Imagining The Next 50 Y (3 AU) [137%]</option>
<option value="HU1001">HU1001 - Intro To Geo &amp; Urban Planning (3 AU)</option>
<option value="ST9001">ST9001 - Intro To Sci,Tech, &amp; Soc (3 AU)</option>
</select>"""
a=a.replace('<select name="subj_code" style="width:350px" size="18" onchange="subj_select(this.form,this.options[this.selectedIndex].value);">',"xxx")
a=a.replace("\n","")
a=a.replace("xxx<option></option>"," ")
a=a.replace("</select>","")
a=a.replace("<option"," ")
a=a.replace("/option>","ß")
a=a.replace("&amp;","&")

a=a.split('ß')


for i in range(len(a)):
    x = a[i]
    for j in range(len(x)):
        if x[j] == '>':
            first = j
        elif x[j] == '<':
            last = j
            break
    a[i] = x[first+1:last]
print(a)