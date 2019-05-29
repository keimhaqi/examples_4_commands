typedef struct pglist_data {
    struct zone node_zones[MAX_NR_ZONES];
    struct zonelist node_zonelists[MAX_ZONELISTS];
    int nr_zones;
    struct page *node_mem_map;
    struct bootmem_data *bdata;
    unsigned long node_start_pfn;
    unsigned long node_present_pages; /* total number of physical pages */
    unsigned long node_spanned_pages; /* total size of physical page
    range, including holes */
    int node_id;
    struct pglist_data *pgdat_next;
    wait_queue_head_t kswapd_wait;
    struct task_struct *kswapd;
    int kswapd_max_order;
} pg_data_t;



struct zone {
    /* Fields commonly accessed by the page allocator */
    unsigned long pages_min, pages_low, pages_high;
    unsigned long lowmem_reserve[MAX_NR_ZONES];
    struct per_cpu_pageset pageset[NR_CPUS];
    /*
    * free areas of different sizes
    */
    spinlock_t lock;
    struct free_area free_area[MAX_ORDER];
    ZONE_PADDING(_pad1_)
    /* Fields commonly accessed by the page reclaim scanner */
    spinlock_t lru_lock;
    struct list_head active_list;
    struct list_head inactive_list;
    unsigned long nr_scan_active;
    unsigned long nr_scan_inactive;
    unsigned long pages_scanned;
    /* since last reclaim */

    unsigned long flags;
    /* zone flags, see below */
    /* Zone statistics */
    atomic_long_t vm_stat[NR_VM_ZONE_STAT_ITEMS];
    int prev_priority;
    ZONE_PADDING(_pad2_)
    /* Rarely used or read-mostly fields */
    wait_queue_head_t * wait_table;
    unsigned long wait_table_hash_nr_entries;
    unsigned long wait_table_bits;
    /* Discontig memory support fields. */
    struct pglist_data *zone_pgdat;
    unsigned long zone_start_pfn;
    unsigned long spanned_pages;
    unsigned long present_pages;
    /* total size, including holes */
    /* amount of memory (excluding holes) */
    /*
    * rarely used fields:
    */
    char *name;
} ____cacheline_maxaligned_in_smp;