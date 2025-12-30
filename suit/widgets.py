from django import forms
from django.forms import Textarea, TextInput, ClearableFileInput
from django.utils.safestring import mark_safe


class AutosizedTextarea(Textarea):
    """
    AutoSized TextArea - TextArea height dynamically grows based on user input
    """

    def __init__(self, attrs=None):
        new_attrs = _make_attrs(attrs, {"rows": 2}, "autosize form-control")
        super(AutosizedTextarea, self).__init__(new_attrs)

    @property
    def media(self):
        return forms.Media(js=("suit/js/autosize.min.js",))

    def render(self, name, value, attrs=None, renderer=None):
        output = super(AutosizedTextarea, self).render(name, value, attrs, renderer)
        output += mark_safe(
            "<script type=\"text/javascript\">django.jQuery(function () { autosize(document.getElementById('id_%s')); });</script>"
            % name
        )
        return output


class CharacterCountTextarea(AutosizedTextarea):
    """
    TextArea with character count. Supports also twitter specific count.
    """

    def render(self, name, value, attrs=None, renderer=None):
        output = super(CharacterCountTextarea, self).render(
            name, value, attrs, renderer
        )
        output += mark_safe(
            "<script type=\"text/javascript\">django.jQuery(function () { django.jQuery('#id_%s').suitCharactersCount(); });</script>"
            % name
        )
        return output


class ImageWidget(ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        html = super(ImageWidget, self).render(name, value, attrs, renderer)
        if not value or not hasattr(value, "url") or not value.url:
            return html
        html = (
            '<div class="ImageWidget"><div class="float-xs-left">'
            '<a href="%s" target="_blank"><img src="%s" width="75"></a></div>'
            "%s</div>" % (value.url, value.url, html)
        )
        return mark_safe(html)


class EnclosedInput(TextInput):
    """
    Widget for bootstrap appended/prepended inputs
    """

    def __init__(
        self,
        attrs=None,
        prepend=None,
        append=None,
        prepend_class="addon",
        append_class="addon",
    ):
        """
        :param prepend_class|append_class: CSS class applied to wrapper element. Values: addon or btn
        """
        self.prepend = prepend
        self.prepend_class = prepend_class
        self.append = append
        self.append_class = append_class
        super(EnclosedInput, self).__init__(attrs=attrs)

    def enclose_value(self, value, wrapper_class):
        if value.startswith("fa-"):
            value = '<i class="fa %s"></i>' % value
        return '<span class="input-group-%s">%s</span>' % (wrapper_class, value)

    def render(self, name, value, attrs=None, renderer=None):
        output = super(EnclosedInput, self).render(name, value, attrs, renderer)
        div_classes = set()
        if self.prepend:
            div_classes.add("input-group")
            self.prepend = self.enclose_value(self.prepend, self.prepend_class)
            output = "".join((self.prepend, output))
        if self.append:
            div_classes.add("input-group")
            self.append = self.enclose_value(self.append, self.append_class)
            output = "".join((output, self.append))

        return mark_safe('<div class="%s">%s</div>' % (" ".join(div_classes), output))


def _make_attrs(attrs, defaults=None, classes=None):
    result = defaults.copy() if defaults else {}
    if attrs:
        result.update(attrs)
    if classes:
        result["class"] = " ".join((classes, result.get("class", "")))
    return result


# Compatibility shims for removed widgets
# These were removed in Django 2.0+ when admin date/time widgets were improved
# Keep these for backward compatibility with third-party packages
class SuitDateWidget(forms.DateInput):
    """
    Backward compatibility shim for SuitDateWidget.
    Uses Django's default DateInput with HTML5 date input type.
    """

    input_type = "date"

    def __init__(self, attrs=None, format=None):
        default_attrs = {"class": "form-control"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs, format=format)


class SuitTimeWidget(forms.TimeInput):
    """
    Backward compatibility shim for SuitTimeWidget.
    Uses Django's default TimeInput with HTML5 time input type.
    """

    input_type = "time"

    def __init__(self, attrs=None, format=None):
        default_attrs = {"class": "form-control"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs, format=format)


class SuitSplitDateTimeWidget(forms.SplitDateTimeWidget):
    """
    Backward compatibility shim for SuitSplitDateTimeWidget.
    Uses Django's default SplitDateTimeWidget with HTML5 inputs.
    """

    def __init__(self, attrs=None, date_format=None, time_format=None):
        widgets = (
            SuitDateWidget(attrs=attrs, format=date_format),
            SuitTimeWidget(attrs=attrs, format=time_format),
        )
        # Skip parent __init__ to avoid double widget creation
        forms.MultiWidget.__init__(self, widgets, attrs)
