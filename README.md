TwitterNames
============

Quick and dirty script to brute-force check availability of Twitter 4-letter handles.

You can supply a prefix to shard/distribute over instances.

Again, this script is dirty, maybe later I will re-write it, but it is not useful beyond finding a short Twitter name :)

There are about 50K 3-letter names - I checked them all and nothing is available.
Took about 4 hours on a single thread.

Later I will check 4-letter names. Since this is 1.8 mln tests - it will take on the order ofseveral days - I will need to somehow break up the work over time and cpus.

It should be doable, as long as Twitter doesn't block your calls. Throttling appears to be okay.

To use:


    python tryNames.py <prefix>



