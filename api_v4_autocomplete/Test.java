public void launchSeed(Integer timepoint) {
    // 寻找在当前时间点需要爬取的种子任务
    Map<Long, CrawlerTask> crawlerSeedTask = crawlerTaskManager.queryCrawlerSeedTasks(3, timepoint);
    if(mapUtils.isAvailable(crawlerSeedTask)){
        Map<Long, DiscoverSeed> seedIdWithDiscoverSeeds = discoverSeedManager.queryBySeedIds(crawlerSeedTask.keySet());
        if(mapUtils.isAvailable(seedIdWithDiscoverSeeds)){
            if (collectionUtils.isAvailable(seedIdWithDiscoverSeeds.values())){
                for(DiscoverSeed discoverSeed : seedIdWithDiscoverSeeds.values()){
                    if(!JinbagUtils.isEmpty(discoverSeed.getSeedUrl()) &&
                            !JinbagUtils.isEmpty(discoverSeed.getSpider())){
                        Map<String, Object> parameters = new HashMap<>();
                        parameters.put("project", discoverProjectName);
                        parameters.put("seed_id", discoverSeed.getSeedId().toString());
                        parameters.put("seed_url", discoverSeed.getSeedUrl());
                        if(!JinbagUtils.isEmpty(discoverSeed.getSpiderMethod())){
                            parameters.put("spider_method", discoverSeed.getSpiderMethod());
                        }
                        parameters.put("spider", discoverSeed.getSpider());
                        String response = restfulInterfaceService.post(discoverModuleEndPoint, parameters);
                        if(!JinbagUtils.isEmpty(response)){
                            logger.info(String.format("Call discover module with param : %s, correspond result is %s.",
                                    jinbagUtils.getNullJsonMapper().toJson(parameters), response));
                        }
                    }
                }
            }
        }
    }
}