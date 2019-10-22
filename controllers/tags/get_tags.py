from controllers import _Controller
from constants import tags
from utils import compile_re

tags_re = {tag: compile_re(tag) for tag in tags}


class GetTagsController(_Controller):
    def __init__(self, request):
        super(GetTagsController, self).__init__(request)

    def _call(self):
        data = self.verify_post_data(
            {"ad_text": "Please specify advertisment text."})
        tags_found = []
        ad_text = data.get("ad_text").lower()
        for tag in tags_re:
            pattern = tags_re.get(tag)
            if tag not in tags_found and pattern.search(ad_text):
                tags_found.append(tag)
        return tags_found
