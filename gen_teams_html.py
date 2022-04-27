"""
$ python3 /Users/saim/github/jsf/gen_teams_html.py | pbcopy
"""
import names 

template = """
<div class="col-lg-6">
    <div class="card shadow border-0 mb-4">
        <div class="row no-gutters">
            <div class="col-md-5 pro-pic"
                style="background:url(images/jsf/team/{num:03d}.jpg) center center no-repeat">
            </div>
            <div class="col-md-7 bg-white">
                <div class="p-4">
                    <h6 class="mb-3">{randomname}</h6>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
                        tempor.
                    </p>
                    <div class="col-md-12 text-center">
                        <ul class="social-network social-circle">
                            <li><a href="#" class="icoFacebook" title="Facebook"><i class="icon-facebook"></i></a></li>
                            <li><a href="#" class="icoTwitter" title="Twitter"><i class="icon-twitter"></i></a></li>
                            <li><a href="#" class="icoLinkedin" title="Linkedin"><i class="icon-linkedin"></i></a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""

count = 0
res = ""
for i in range(30 + 1):
    if i % 2 == 0:
        res += '\n<div class="row">'
    res += template.format(num=i + 1, randomname=names.get_full_name())
    if i % 2 != 0:
        res += '\n</div>'


print(res)

