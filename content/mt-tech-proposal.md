Title: Technology Proposal for MT
Date: 2013-10-28 19:00
Author: nocoolnametom
Category: Mormonism
Tags: web development, mormonthink, pelican, prose
Slug: mt-tech-proposal
Lang: en


MT has become, without a doubt, one of the most influential websites of its kid on the Internet.
Both beloved and vilified because of their reach and their fame, the editors of MT should be proud
of what they have been able to accomplish.

However, the Internet moves fast and staying still means falling behind.  If MT wants to continue to
inspire thought and research they need to move away from a paradigm of disseminating information
outwards to a new paradigm where the editors are not just content producers but are more traditional
editors of content provided by a wide variety of sources.  Response time to research, both in terms
of advancing new findings as well as removing incorrect facts, will become more important in the
future as sources of information continue to widen.

Recently, MT underwent a much-needed design and layout change.  It is very much appreciated, but we
can and need to move further than just a redesign.  However, there are two groups who have different
needs that must be satisfied in any future planning.

The editors need a solution where creating and editing content is as easy as possible.  However,
developers and designers need a solution that removes as much of the display layout and logic from
the content as possible.  CMS's such as Wordpress usually provide a great middle road by providing
simple content editing that is later combined with the site layout after editing.  However, CMS's as
a technology are complex and are targets for security flaws, and when combined with multiple users
of various permission levels can quickly become immensely complex for an average user.


Static Site Generators
----------------------

One halfway point between the needs of the content creators and the web developers is the new idea
of static site generation.  A static site generator does not store the content in a database, but
rather stores content in text files (usually Markdown or ReStructuredText).  Upon command, the
content files can be "compiled" with a site layout to produce a collection of HTML files ready to be
deployed to a simple web server.  Most web developers are familiar with the development pattern of
Model-View-Controller.  In a very rough (read: wrong) summary, the idea of an MVC web app like
Wordpress is that the Model is the content written by the users, which is interpreted by a
Controller, to produce (usually in conjunction with a template) a View for the end user to see.  A
static site generator could be though of as a Model-View-Controller pattern where all possible views
are pre-built and saved as files.

The benefits, from a web developer's viewpoint, of a Static Site Generator (SSG) are speed and
security.  When a page is requested from the server there is no interpreter to be run, no
specialized compilations to perform.  Instead the server just grabs the HTML file in question and
serves it.  Files can be browser and cache-able, as well as compressed, providing even more speed
improvements.  And from a security point of view when there are no actual moving parts there are no
vectors for attack: no SQL injections to guard against, no Status 500 errors to exploit.  Also, the
hardware needs of the server are at their most minimal.

Of course that describes the current site, which is also flat files.  But the current site does
nothing to separate the concerns of the content creators and the developers.  Using a SSG means that
the content itself is still stored separately from the site layout.  Extensive modifications can be
performed upon the look, feel, and behavior of a page without altering the content and vice-versa.


Markdown
--------

Markdown, as a formatting language, is becoming more and more well-known.  It is the formatting
language used by many popular websites, such as GitHub and Reddit.  Chances are that the editors and
other content contributors are already quite familiar with it (it is the formatting language used by
Reddit, for instance, and we know that many of the MT editors are active on Reddit).  This proposal
itself was written in Markdown (not that this is much of a big deal as it isn't really using much
formatting).  You can [see the original file here,][] if you'd like.


GitHub
------

One other benefit of moving the content pages to their own files is that it becomes far easier to
make and track changes to them.  The penultimate piece of this new technology system for MormonThink
would consist of hosting the entire source code for the site publicly at GitHub.  I understand that
this extreme transparency might make a lot of people nervous, but in the end MormonThink is devoted
to facts, truth, and accuracy and transparency is one of the best ways to force these ideals in
technology.

Also, having the source at GitHub introduces an entirely new aspect to the development of
MormonThink for the future: additional content.  As a public repository of code, anyone would have
the freedom to download their own copy of the website to do with as they wish.  In reality, there is
nothing about this process that is now impossible and indeed I've had to copy every accessible file
from MormonThink as I've pursued this project.

GitHub, and its underlying technology of git, are centered around this idea of widely distributed
code because of how those widely separated copies of the code can be used to make the project
better.  Users can do more than just make a copy of the code: they can alter it (creating what is
called a "fork" of the code).  In the case of the future MormonThink site they can add new pages or
even entire sections, they can clean up and alter existing pages, they can upload images, and much
more.  This is because they have full control over their own copy of the code.  Again, there is
*nothing* preventing this behavior even now so while this might sound quite scary it really isn't.
Anyone can post their own altered version of MormonThink even now, but these unofficial versions
have no hope of attaining anywhere *near* the audience they need to endanger the fame and authority
of the current site.  Opening up the code would not change this: MormonThink.com is still the
official page.

But users can *request* that their changes be "merged" back into the official code (the technical
term for this request is a "pull request").  And here is where the editors of MormonThink get to
continue to be **editors.**  GitHub has extensive tools set up around users and permissions involved
with these merges.  This process of third-party, independent coders and content creators
contributing their own effort back to the main project is how open source projects like Linux are
built.  Allowing these requests is fully the responsibility of the owners of the original GitHub
repository.


Example
-------

Let's assume that it's now a year in the future.  The existing pages of MormonThink have been
migrated to a combination of Markdown content pages being compiled by a Static Site Generator like
Pelican or Jekyll.  The source code, including all of these content pages, are publicly accessible
at MormonThink's GitHub repository.  A reader, let's call her Janet Law, notices that there's an
error on a page, say the page about the Expositor affair.  She wants to know how to fix it and sees
a link at MormonThink about how to contribute.  There she finds a set of simple instructions that
lead her to create an account a GitHub and to fork the code for MormonThink.  Now she has her own
personal copy of the code.  She opens up the files that discuss the Expositor history and makes the
changes she thinks need to be made and saves them to her personal copy.  Now she initiates a "pull
request" to MormonThink asking them to merge her changes back into the main website.  A MT editor
sees her pull request and takes a look at the changes.  GitHub color-codes the changed files so that
it is easy to see exactly where changes have been made.  The editor, while impressed, is concerned
about one or two of the changes.  He comments on the pull request asking Janet Law for more
information on one point and to rewrite another point.  Janet makes those changes to her personal
copy and saves it again.  Now her pull request is asking to merge in all of those changes, too.  The
editor takes another look at the request and decides that it's a good change and he approves the
request.  With that approval Janet's changes are now incorporated into the official website.  If
there are any problems it's not very difficult to roll the site back to a previous version of the
code as git, the technology underlying GitHub, keeps a full and complete record of every change made
to the code and can roll back and forwards the active code easily.

In our example we still have an official MT editor, but now much of the content development and
maintenance can be moved from their own responsibility to a wide army of volunteers who want to
help.  Of course, every editor can go through the same process and approve their own merges if they
also want to add content, but they are now editors in a very real sense.

(Also, as a quick aside, the created content does not only need to be in English!  Translations of
MT content are sorely lacking, and opening up the code and the contribution process this way would
do wonders for the ability of foreign language speakers and writers to quickly amass a large amount
of translated copy.)


Prose
-----

There's one final benefit in this example layout: it can be done without opening any code tool such
as Dreamweaver or Sublime Text.  For Markdown files contained in a GitHub repository there is a
tool, called [Prose][], that can edit them on-line and save the changes to the personal or official
code repositories.  Prose is a great tool because it can instantly translate the Markdown being
written into a rough formatted version so that an author can quickly make sure that they're writing
and formatting their content the way they want.


Healthcare.gov (Not the Bad Bits!)
----------------------------------

This technology plan for MormonThink isn't just an unproven idea.  While the actual application
parts of the website have been bogged down in bugs and errors, the landing pages and informational
pages for the US government site [healthcare.gov][] are produced using a Static Site Generator, a
private instance of GitHub, and Prose.  These aspects of the website have been lauded for their
simple design and devotion to user-friendliness.  It *does* kinda stick that the rest of the site is
so buggy because it certainly reflects badly on the parts of the site served with the SSG.


Conclusion
----------

The future of MormonThink requires some drastic changes (we didn't even get into the fact that quite
a bit of their current content is heavily dependent upon tables of data and while these don't need
to be deleted they shouldn't be the main content for average users to read).  I want to propose that
these changes should include moving the website to an open source model that would allow to wide
involvement from users across the world.  In my opinion, the best way to adopt an open-source model
would be the use of a Static Site Generator, such as Jekyll or Pelican, combined with Markdown
content source files.  This very blog is actually produced via the same process.  The difficulty in
setting it up would involve the initial transition.  Once set up, maintenance and continuing content
creation would be very easy and manageable with a shallow learning curve no more difficult than the
current process of local file editing via Dreamweaver and upload via FTP.

I welcome any and all comments and questions.  For anyone who is interested you can find my current
explorations of this project at the following two repositories:

 * **[nocoolnametom/MT-Transfer][]** - This is a scraper I'm spun up in some free time that rips the
                                       existing site and converts it (mostly) into Markdown files
                                       that can be used with a SSG.

 * **[nocoolnametom/MormonThink][]** - This is my attempt at creating a SSG-served version of the
                                       site using the files from the scraper.  I'm not very far
                                       along on this project, obviously.

[see the original file here,]: |filename|mt-tech-proposal.md
[Prose]: http://developmentseed.org/blog/2012/june/25/prose-a-content-editor-for-github/
[healthcare.gov]: http://healthcare.gov/
[nocoolnametom/MT-Transfer]: https://github.com/nocoolnametom/MT-Transfer
[nocoolnametom/MormonThink]: https://github.com/nocoolnametom/MormonThink