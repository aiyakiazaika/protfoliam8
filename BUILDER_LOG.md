# Capstone — Portfolio Site
## TASKS

Task 1. Scaffold the repo and write CLAUDE.md with stack conventions and constraints.
Verify: CLAUDE.md exists and defines Flask, no JS frameworks, contact form is UI-only.

Task 2. Create base Flask app with homepage route and base HTML template.
Verify: `python app.py` runs, localhost:5000 loads without errors.

Task 3. Build the base layout and navigation (header, footer, nav links).
Verify: All nav links render, page looks clean, no broken links.

Task 4. Build the Projects section with static project cards (title, description, tags).
Verify: All 5 projects show on the page with correct info.

Task 5. Add media support — images and videos embed per project card.
Verify: Drone club video plays, robotics/docking images load, no broken media.

Task 6. Build the About section with bio, skills, and trilingual/background info.
Verify: Section renders with correct content, reads naturally.

Task 7. Build the Contact form (name, email, message fields — UI only, no backend send).
Verify: Form renders, fields are labeled, submit button shows a success message.


//haven't added yet will add later
Task 8. Add a dedicated page or modal for each project with more detail and media.
Verify: Clicking a project card opens the detail view with full description and media.

Task 9. Style the full site — consistent colors, fonts, mobile-friendly layout.
Verify: Site looks polished on both desktop and mobile browser window.

Task 10. Write tests for routes (homepage, contact, project pages return 200).
Verify: pytest passes for all routes with no errors.

Task 11. Write README.md with what the site is, how to run it, and stack used.
Verify: A stranger could clone and run it using only the README.

Task 12. Full manual walkthrough — click every link, view every project, submit the form.
Verify: Nothing is broken, all media loads, form shows success message.


## BUILDER_LOG

## Task 1 
- Brief: basically creating a CLAUDE.md for claude to follow and have a set of rules 
- What Claude proposed: it just read the rules and guidelines because I created it

## Task 2
- Brief: 
- What Claude proposed: it made a base.html file and index.html where we have the basic code for the website
- What I changed before approving: I added diffrent sections according to my extracurriculars: <p>Robotics &bull; Drones &bull; Research &bull; Space</p>
- Verification: I ean python app.py & opened the website http://127.0.0.1:5000
- One thing I learned: I learned I don't have to learn all specifics of HTML i can easily get claude to build me the structure also I learned u need to be specific with what you ask for or else claude will assume

## Task 3
- Brief: Built the base layout and navigation (header, footer, nav links).
- What Claude proposed: 
    static/style.css:
  - html { scroll-behavior: smooth } — clicking nav links scrolls smoothly to each section
  - Header is now position: sticky; top: 0 with a subtle box shadow — stays visible while scrolling

  - Nav link hover now turns blue (#0066cc) instead of underline
  - Footer links styled
  - Mobile media query at 600px
  - nav wraps, padding tightens,
   hero font scales down

  templates/base.html:

  - Footer now includes GitHub
  and LinkedIn link placeholders

- What I changed before approving: I added the links for my git and linkedin
- Verification: I verified by runing python app.py and http://127.0.0.1:5000 where I saw and scrolled the page to see the nav 
that stuck out to the top, I also clicked the links and checked the smooth scroll.
- One thing I learned: I learned claude is a good tool for website building 

## Task 4
- Brief: this is the part where we plug the descriptions for my activities
- What Claude proposed: it asked for 1-2 sentece descriptions 
- What I changed before approving: i fed it some bullet points from my resume and told it not to do a longer description
- Verification: python.app py and scroll to the Projects section to see all 5 cards of activies
- One thing I learned: I learned claude is fast and can replicate exactly what I ask for efficiently. Addtionally you should stop
and redirect it when needed. 

## Task 5
- Brief: here we add different media: images and videos 
- What Claude proposed: It asked me 2 questions and I chose the best option for my case
● Do you have actual media files to upload (drone video, robotics photos, etc.), or should I build the media support infrastructure now and
   use placeholders until you add real files later?
   → Use placeholders now
 ● Where should media appear — on the project cards on the homepage, or only on the detail pages (Task 8)?
   → Cards on homepage
- What I changed before approving: I chose placeholders for now because I wanted it to work without interuptions in one flow which I think would waste less tokens, and later I could just add whatever images and videos I want without prompting it
multiple times for each picture and video
- Verification: ran python app.py again and made sure there was a place for the media
- One thing I learned: Tryin to be smart with tokens because I'm running out. So what I'll do is drop pics into static/images/ or static/videos/ and update the filename in app.py — the card updates automatically. For the drone video, add drone-club.mp4 to static/videos/ and it'll play right in the card.
I had an issue with trying to uplaod the files but it eventually worked out when I figured out how to drop them into the folder in a way that claude & vs code can access them

## Task 6
- Brief: adding the about section
- What Claude proposed: it proposed i give it a description paragraph however I decided I wanted it to look at my resume
and see if it wants anything specific from it
- What I changed before approving: I changed the paragraph about me to specific things about me like knowing languages, my education, awards, certifications, skills etc
- Verification: I ran python app.py and checked the website to make sure it looks right
- One thing I learned: making my own decisions, doesnt matter what claude asks me or plans i decide whats actually best
and what it suggest isn't always right 

## Task 7
- Brief: contact section filled out, allowing visitors to contact me!
- What Claude proposed:   
- Form — Name, Email, Message fields with labels, a blue Submit button, max-width 560px
  - Submit — POSTs to /contact, Flask redirects to /?sent=1#contact (no email sent, no external calls)
  - Success message — green-tinted box with a checkmark replaces the form when ?sent=1 is in the URL
- I didn't change anything, it worked. Just needed to add a readme.md file thats it.




//for future
## Task 8
- Brief: 
- What Claude proposed: 
- What I changed before approving: 
- Verification: 
- One thing I learned: 

## Task 9
- Brief: 
- What Claude proposed: 
- What I changed before approving: 
- Verification: 
- One thing I learned: 

## Task 10
- Brief: 
- What Claude proposed: 
- What I changed before approving: 
- Verification: 
- One thing I learned: 

## Task 11
- Brief: 
- What Claude proposed: 
- What I changed before approving: 
- Verification: 
- One thing I learned: 

## Task 12
- Brief:
- What Claude proposed: 
- What I changed before approving: 
- Verification: 
- One thing I learned: 