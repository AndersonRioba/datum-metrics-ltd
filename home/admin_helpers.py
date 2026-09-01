# home/admin_helpers.py
# Badge count callbacks referenced from the UNFOLD sidebar navigation config.


def new_inquiries_badge(request):
    """Show count of unread/new contact inquiries in the sidebar."""
    from home.models import ContactInquiry

    count = ContactInquiry.objects.filter(status="new").count()
    return str(count) if count else None


def blogpost_badge(request):
    """Show count of unpublished draft blog posts in the sidebar."""
    from home.models import BlogPost

    count = BlogPost.objects.filter(is_published=False).count()
    return str(count) if count else None
