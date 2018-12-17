curl -X POST 'http://192.168.1.105:6800/schedule.json?project=discoverModule&spider=amazon_best_sellers_spider&seed_url=https://www.amazon.com/Best-Sellers-Home-Kitchen/zgbs/home-garden/ref=zg_bs_nav_0'

curl -X POST -d '
{
  "project":"discoverModule",
  "spider":"amazon_best_sellers_spider",
  "seed_id":10,
  "seed_url":"https://www.amazon.com/Best-Sellers-Home-Kitchen/zgbs/home-garden/ref=zg_bs_nav_0" 
}
' http://192.168.1.105:6800/schedule.json