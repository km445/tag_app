import re

from controllers import _Controller
from constants import tags


class GetTagsController(_Controller):
    def __init__(self, request):
        super(GetTagsController, self).__init__(request)

    def _call(self):
        data = self.verify_post_data(
            {"ad_text": "Please specify advertisment text."})
        tags_found = []
        ad_text = data.get("ad_text").lower()
        words = re.findall(r"[\w']+", ad_text)
        for tag in tags:
            if tag not in tags_found:
                tag_parts = tag.split()
                amount_of_tag_parts = len(tag_parts)
                matched_tag_parts = 0
                if tag_parts and tag_parts[0] in words:
                    last_tag_part_index = words.index(tag_parts[0])
                    for tag_part in tag_parts:
                        if tag_part in words[last_tag_part_index:
                                             last_tag_part_index + 3]:
                            matched_tag_parts += 1
                            last_tag_part_index = words.index(tag_part) + 1
                    if amount_of_tag_parts == matched_tag_parts:
                        tags_found.append(tag)
        return tags_found
