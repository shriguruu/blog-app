from blog.models import Post
from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    help = 'This command populates the database with post data'

    def handle(self, *args:Any, **options:Any):
        Post.objects.all().delete()  # Clear existing data
        titles = [
            "Unlocking the Power of Python for Data Science",
            "A Backpacker's Guide to Southeast Asia",
            "The Art of Deep Work in a Distracted World",
            "Mastering the Perfect Sourdough Bread at Home",
            "Exploring the Hidden Gems of Chennai"
        ]

        contents = [
            """
            Python continues to dominate the world of data science, and for good reason. Its simple syntax, powerful libraries like Pandas, NumPy, and Scikit-learn, and a vibrant community make it the go-to language for analysts and machine learning engineers. 
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            """,
            """
            Traveling through Southeast Asia on a budget is an unforgettable experience. From the bustling streets of Bangkok to the serene temples of Angkor Wat, the region offers a diverse tapestry of cultures, cuisines, and landscapes. This guide provides essential tips for first-time backpackers.
            
            Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem. Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Proin eget tortor risus. Pellentesque in ipsum id orci porta dapibus.
            """,
            """
            In an age of constant notifications and digital noise, the ability to focus without distraction is a superpower. Cal Newport's concept of 'Deep Work' offers a path forward, enabling you to produce high-quality work in less time. 
            
            Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit. Cras ultricies ligula sed magna dictum porta. Nulla quis lorem ut libero malesuada feugiat.
            """,
            """
            Baking sourdough bread can seem intimidating, but with a little patience and the right technique, anyone can achieve that perfect crust and airy crumb. It all starts with a healthy starter.
            
            Donec sollicitudin molestie malesuada. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus suscipit tortor eget felis porttitor volutpat. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Sed porttitor lectus nibh.
            """,
            """
            Beyond the well-trodden paths of Marina Beach and Kapaleeshwarar Temple lies a Chennai teeming with hidden gems. This guide will take you through some of my favorite lesser-known spots in the city, from quiet, artistic cafes to serene stretches of coastline.
            
            Nulla porttitor accumsan tincidunt. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. Quisque velit nisi, pretium ut lacinia in, elementum id enim.
            """
        ]

        img_urls = [
            "https://picsum.photos/seed/python/900/600",
            "https://picsum.photos/seed/travel/900/600",
            "https://picsum.photos/seed/productivity/900/600",
            "https://picsum.photos/seed/sourdough/900/600",
            "https://picsum.photos/seed/chennai/900/600"
        ]

        for title, content, img_url in zip(titles, contents, img_urls):
            Post.objects.create(title=title, content=content, img_url=img_url)
        
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))