from blog.models import Post, Category
from django.core.management.base import BaseCommand
from typing import Any
import random

class Command(BaseCommand):
    help = 'This command populates the database with post data'

    def handle(self, *args:Any, **options:Any):
        Post.objects.all().delete()  # Clear existing data
        titles = [
            "Unlocking the Power of Python for Data Science",
            "A Backpacker's Guide to Southeast Asia",
            "The Art of Deep Work in a Distracted World",
            "Mastering the Perfect Sourdough Bread at Home",
            "Exploring the Hidden Gems of Chennai",
            "Beginner's Guide to Investing in the Stock Market",
            "The 15-Minute Daily Workout for Busy Professionals",
            "Demystifying Blockchain: Beyond Cryptocurrency",
            "From Bean to Cup: A Guide to Brewing the Perfect Coffee",
            "How to Transform Your Balcony into a Green Oasis",
            "Ace Your Next Virtual Job Interview: Tips and Tricks",
            "The Future of Space Exploration: Mars and Beyond",
            "Forgotten Empires: The Rise and Fall of the Chola Dynasty",
            "The Evolution of Indian Classical Music",
            "An Introduction to Digital Painting for Beginners",
            "Sustainable Living: 10 Easy Swaps for a Greener Home",
            "Mindfulness and Meditation: A Practical Guide to a Calmer Mind",
            "Weekend Getaways from Bangalore You Can't Miss",
            "Mastering Manual Mode: A Beginner's Photography Guide",
            "Book Review: 'Atomic Habits' by James Clear"
        ]

        contents = [
            """
            Python continues to dominate the world of data science, and for good reason. Its simple syntax, powerful libraries like Pandas, NumPy, and Scikit-learn, and a vibrant community make it the go-to language for analysts and machine learning engineers. 
            
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            """,
            """
            Traveling through Southeast Asia on a budget is an unforgettable experience. From the bustling streets of Bangkok to the serene temples of Angkor Wat, the region offers a diverse tapestry of cultures, cuisines, and landscapes. This guide provides essential tips for first-time backpackers.
            
            Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem. Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui.
            """,
            """
            In an age of constant notifications and digital noise, the ability to focus without distraction is a superpower. Cal Newport's concept of 'Deep Work' offers a path forward, enabling you to produce high-quality work in less time. 
            
            Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit. Cras ultricies ligula sed magna dictum porta.
            """,
            """
            Baking sourdough bread can seem intimidating, but with a little patience and the right technique, anyone can achieve that perfect crust and airy crumb. It all starts with a healthy starter.
            
            Donec sollicitudin molestie malesuada. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus suscipit tortor eget felis porttitor volutpat.
            """,
            """
            Beyond the well-trodden paths of Marina Beach and Kapaleeshwarar Temple lies a Chennai teeming with hidden gems. This guide will take you through some of my favorite lesser-known spots in the city, from quiet, artistic cafes to serene stretches of coastline.
            
            Nulla porttitor accumsan tincidunt. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula.
            """,

            """
            Dipping your toes into the stock market can feel overwhelming, but it's one of the most effective ways to build long-term wealth. This guide breaks down the basics of stocks, diversification, and how to make your first investment.
            
            Proin eget tortor risus. Pellentesque in ipsum id orci porta dapibus. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem.
            """,
            """
            Finding time to exercise can be tough. This high-intensity interval training (HIIT) routine is designed for maximum impact in just 15 minutes, helping you stay fit and energized without disrupting your packed schedule.
            
            Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Cras ultricies ligula sed magna dictum porta. Curabitur aliquet quam id dui posuere blandit. Nulla quis lorem ut libero malesuada feugiat.
            """,
            """
            When most people hear 'blockchain,' they think of Bitcoin. But the underlying technology has the potential to revolutionize industries from finance to healthcare. We'll explain how it works in simple, easy-to-understand terms.
            
            Donec rutrum congue leo eget malesuada. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Sed porttitor lectus nibh. Vivamus suscipit tortor eget felis porttitor volutpat.
            """,
            """
            The journey of a coffee bean from the farm to your cup is a fascinating one. Learn about different brewing methods like Pour-Over, French Press, and AeroPress to elevate your morning coffee ritual.
            
            Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sollicitudin molestie malesuada. Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus.
            """,
            """
            Even the smallest urban spaces can become a source of joy and greenery. This guide will walk you through choosing the right plants, pots, and soil to create a beautiful and thriving balcony garden, no matter the size.

            Sed porttitor lectus nibh. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Nulla porttitor accumsan tincidunt. Quisque velit nisi, pretium ut lacinia in, elementum id enim.
            """,
            """
            The era of remote work has made virtual interviews the new norm. Learn how to set up your tech, present yourself professionally, and answer common questions with confidence to land your dream job from home.
            
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            """,
            """
            Humanity is on the brink of a new era in space travel. With missions planned for Mars and beyond, we're closer than ever to becoming an interplanetary species. We explore the technology and challenges that lie ahead.
            
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            """,
            """
            Long before the Mughals, the Chola Dynasty of Southern India reigned supreme, leaving a legacy of stunning temples and maritime trade. Journey back in time to explore the history of this powerful and often overlooked empire.

            Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem. Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui.
            """,
            """
            From the ancient Vedic hymns to modern fusion, Indian classical music has a rich and complex history. This article explores the core concepts of Raga and Tala and introduces the key figures who have shaped this timeless art form.

            Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Donec rutrum congue leo eget malesuada. Curabitur aliquet quam id dui posuere blandit. Cras ultricies ligula sed magna dictum porta.
            """,
            """
            Have you always wanted to create digital art? With today's powerful software and affordable tablets, it's never been easier to get started. This tutorial covers the basics of layers, brushes, and color theory in digital painting.
            
            Donec sollicitudin molestie malesuada. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus suscipit tortor eget felis porttitor volutpat.
            """,
            """
            Creating a sustainable home doesn't require a massive overhaul. By making small, conscious changes, you can significantly reduce your environmental impact. Here are 10 simple swaps you can make today.
            
            Nulla porttitor accumsan tincidunt. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula.
            """,
            """
            In our fast-paced world, finding moments of peace is essential for mental well-being. This practical guide introduces the core principles of mindfulness and provides simple meditation exercises to help you reduce stress and live in the present.
            
            Sed porttitor lectus nibh. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Nulla porttitor accumsan tincidunt. Quisque velit nisi, pretium ut lacinia in, elementum id enim.
            """,
            """
            Need a break from the hustle of Bangalore? From the misty hills of Coorg to the ancient ruins of Hampi, we've curated a list of perfect weekend destinations, all just a short drive or train ride away.

            Proin eget tortor risus. Pellentesque in ipsum id orci porta dapibus. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem.
            """,
            """
            Switching your camera to Manual mode is the single best way to take creative control over your photos. This guide demystifies the 'exposure triangle'—Aperture, Shutter Speed, and ISO—to help you capture stunning images.
            
            Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Cras ultricies ligula sed magna dictum porta. Curabitur aliquet quam id dui posuere blandit. Nulla quis lorem ut libero malesuada feugiat.
            """,
            """
            James Clear's 'Atomic Habits' argues that tiny, incremental changes are the key to achieving remarkable results. In this review, we explore the core concepts of the book and how you can apply them to build better habits in your own life.

            Donec rutrum congue leo eget malesuada. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Sed porttitor lectus nibh. Vivamus suscipit tortor eget felis porttitor volutpat.
            """
        ]

        img_urls = [
            "https://picsum.photos/seed/python/900/600",
            "https://picsum.photos/seed/travel/900/600",
            "https://picsum.photos/seed/productivity/900/600",
            "https://picsum.photos/seed/sourdough/900/600",
            "https://picsum.photos/seed/chennai/900/600",
            "https://picsum.photos/seed/investing/900/600",
            "https://picsum.photos/seed/fitness/900/600",
            "https://picsum.photos/seed/blockchain/900/600",
            "https://picsum.photos/seed/coffee/900/600",
            "https://picsum.photos/seed/garden/900/600",
            "https://picsum.photos/seed/interview/900/600",
            "https://picsum.photos/seed/space/900/600",
            "https://picsum.photos/seed/history/900/600",
            "https://picsum.photos/seed/music/900/600",
            "https://picsum.photos/seed/digitalart/900/600",
            "https://picsum.photos/seed/green/900/600",
            "https://picsum.photos/seed/meditation/900/600",
            "https://picsum.photos/seed/bangalore/900/600",
            "https://picsum.photos/seed/camera/900/600",
            "https://picsum.photos/seed/habits/900/600"
        ]

        categories = Category.objects.all()

        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)
        
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))