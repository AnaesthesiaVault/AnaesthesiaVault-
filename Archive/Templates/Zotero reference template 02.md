> [!Cite]
> {{bibliography}}
>[!Synth]
>**Contribution**::
>[!md]
> {%- for creator in creators %} {%- if creator.name == null %} **{{creator.creatorType | capitalize}}**:: {{creator.lastName}}, {{creator.firstName}}{%- endif -%}<br>
> {%- if creator.name %}**{{creator.creatorType | capitalize}}**:: {{creator.name}}{%- endif -%}{%- endfor %} 

[> **Title**:: {{title}}  
> **Year**:: {{date | format("YYYY")}}   
> **Citekey**:: @{{citekey}}  
> {%- if itemType %}**itemType**:: {{itemType}}{%- endif %}  
> {%- if itemType == "journalArticle" %}**Journal**:: *{{publicationTitle}}* {%- endif %}  
> {%- if volume %}**Volume**:: {{volume}} {%- endif %}  
> {%- if issue %}**Issue**:: {{issue}} {%- endif %}   
> {%- if itemType == "bookSection" %}**Book**:: {{publicationTitle}} {%- endif %}  
> {%- if publisher %}**Publisher**:: {{publisher}} {%- endif %}  
> {%- if place %}**Location**:: {{place}} {%- endif %}   
> {%- if pages %} **Pages**:: {{pages}} {%- endif %}  
> {%- if DOI %}**DOI**:: {{DOI}} {%- endif %}  
> {%- if ISBN %}**ISBN**:: {{ISBN}} {%- endif %}]
URL: {{url}}>)
Zotero Link: {{pdfZoteroLink}}

> [!Abstract]  
> {%- if abstractNote %}  
> {{abstractNote}}  
> {%- endif -%}


[{% for annotation in annotations -%} 
    {%- if annotation.annotatedText -%} 
    {{annotation.annotatedText}}”{% if annotation.color %} {{annotation.colorCategory}} {{annotation.type | capitalize}} {% else %} {{annotation.type | capitalize}} {% endif %}[Page {{annotation.page}}](zotero://open-pdf/library/items/{{annotation.attachment.itemKey}}?page={{annotation.page}}&annotation={{annotation.id}}) 
    {%- endif %} 
    {%- if annotation.imageRelativePath -%}
    ![[{{annotation.imageRelativePath}}]] {%- endif %} 
{% if annotation.comment %} 
{{annotation.comment}} 
{% endif %} 
{% endfor -%}](<{%- macro calloutHeader(type, color) -%}
{%- if type == "highlight" -%}
%3Cmark style="background-color: {{color}}"%3EHighlight</mark>
{%- endif -%}
{%- if type == "text" -%}
Note
{%- endif -%}
{%- endmacro -%}
{%- set annots = annotations | filterby("date", "dateafter", lastExportDate) -%}
{%- if annots.length > 0 %}
### Exported: {{exportDate | format("YYYY-MM-DD h:mm a")}}
{% for annot in annots -%}
> {{calloutHeader(annot.type, annot.color)}}
{%- if annot.annotatedText %}
> {{annot.annotatedText | nl2br}}
{%- endif -%}
{%- if annot.imageRelativePath %}
> ![[{{annot.imageRelativePath}}]]
{%- endif %}
> [page {{annot.page}}](file://{{annot.attachment.path | replace(" ", "%20")}}) [[{{annot.date | format("YYYY-MM-DD#h:mm a")}}]]
{%- if annot.comment %}
> - {{annot.comment | nl2br}}
{% endif %}
{% endfor -%}
{% endif -%}>)






---

**Copyright**
© 2022 Francois Uys. All Rights Reserved.
