directory_sync
==============

An advanced file synchronization program that utilizes mongo-db for configuration storage.

This program initializes directories to sync and rules to apply by loading in either json documents locally or from mongoDB documents (useful for systems that need to access these elements across multiple systems)

Program initializes and will filter out all the improper files based upon file rules and blocks that are implemented in these rules.

Right Now, the program is not concurrent and can block on your machine for certain syncs. I'm currently syncing about 20 gigs / 70,000 files and it makes my computer unusable for about 5 minutes while initializing.

I'm planning a rebuild in Go to make this run a bit quicker. Will implement a front-end api in ruby / python.