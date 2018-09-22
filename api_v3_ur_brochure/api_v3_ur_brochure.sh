curl -i -k -H 'Content-Type: application/json' -d '
{
  "user": "289",
  "num": 10,
  "blacklistItems":[52,40,60,84],
  "blacklist":[9652038,10183072,6467258,10651960,10651982,423595,10651980,10651992],
  "fields":[
    {"name": "status", "values":[0]}
  ]
}
' http://localhost:9125/api/v3/ur/brochure

if(mapUtils.isAvailable(articleProduct)){
            for(Map.Entry<Integer, List<Integer>> entry : articleProduct.entrySet()){
                productIds.addAll(entry.getValue());
                if(collectionUtils.isAvailable(entry.getValue())){
                    for(Integer productId : entry.getValue()){
                        if(collectionUtils.isAvailable(blacklist)){
                            if(!blacklist.contains(productId)){
                                productWithScore.put(productId, 0.);
                            }
                        }
                    }
                }
            }
        }


curl -i -k -H 'Content-Type: application/json' -d '
{
  "user": "289",
  "num": 1,
  "blacklistItems":[52,40,60,84],
  "blacklist":[4737838,6046746,6244222,6244508,6244058,6244250,1582830,6244322,6244432,6244544,10154666,10188058,10428602,10390276,10339794,9313678,7672980,10318382,10479892,10387808,10543904,10548912,10551138,10480506,10552292,10553338,10508542,10543850,10553644,10553374,10553904,10555936,10558816,10558290,10559332,10554358,10555818,10559222,10556044,10554558,10560720,10562048,10565824,10563762,10564754,10567942,10561882,10565754,10565818,10567078,10576608,10579008,10580306,10584758,10583016,10584570,10583436,10583820,10583310,10583528,10586592,10585954,10585540,10586086,10585804,10586668,10585550,10585662,10587054,10585226,10587234,10587286,10587176,10587288,10587528,10587704,10587178,10587100,10587756,10587590],
  "fields":[
    {"name": "status", "values":[0]}
  ]
}
' http://localhost:9124/api/v3/ur/brochure


curl -i -k -H 'Content-Type: application/json' -d '
{
  "user": "289",
  "num": 1,
  "blacklistItems":[52,40,60,84],
  "blacklist":[10651560,10665990,10759370],
  "fields":[
    {"name": "status", "values":[0]}
  ]
}
' http://localhost:9124/api/v3/ur/brochure


productIds = {LinkedHashMap$LinkedKeySet@13275}  size = 10
10651560,10459046,10776126,10699482,10759370,10676168,10681872,10821472,10665990,10853170

10651560,
{"promo":{"productId":55,"shareTitleEn":"$125.00 Printed Short-Sleeve Polo","titleEn":"Saks Fifth Avenue - $125.00 Printed Short-Sleeve Polo","vendorId":13816,"productImageLink":"https://image.s5a.com/is/image/saks/0400095747459_500x500.jpg"},"product":{"productId":55,"lastCheckedTime":1483250400000,"productSale":"$125.00","productPrice":"$125.00","sourceId":13816,"productTitle":"Printed Short-Sleeve Polo","productImageLink":"https://image.s5a.com/is/image/saks/0400095747459_500x500.jpg"}}


10459046


4737838,6046746,6244222,6244508,6244058,6244250,1582830,6244322,6244432,6244544,10154666,10188058,10428602,10390276,10339794,9313678,7672980,10318382,10479892,10387808,10543904,10548912,10551138,10480506,10552292,10543850,10553338,10553644,10508542,10553374,10553904,10555936,10558816,10558290,10559332,10554358,10559222,10555818,10556044,10554558,10560720,10562048,10565824,10563762,10564754,10567078,10567942,10561882,10565754,10565818,10576608,10579008,10580306,10584758,10583016,10583528,10584570,10583436,10583820,10583310,10586592,10585954,10585540,10586086,10585226,10585804,10586668,10585550,10585662,10587054



SELECT * FROM `article_product` WHERE `product_id` not in (4737838,6046746,6244222,6244508,6244058,6244250,1582830,6244322,6244432,6244544,10154666,10188058,10428602,10390276,10339794,9313678,7672980,10318382,10479892,10387808,10543904,10548912,10551138,10480506,10552292,10543850,10553338,10553644,10508542,10553374,10553904,10555936,10558816,10558290,10559332,10554358,10559222,10555818,10556044,10554558,10560720,10562048,10565824,10563762,10564754,10567078,10567942,10561882,10565754,10565818,10576608,10579008,10580306,10584758,10583016,10583528,10584570,10583436,10583820,10583310,10586592,10585954,10585540,10586086,10585226,10585804,10586668,10585550,10585662,10587054
) and `article_id` in (1090, 1088, 1086, 1084, 1082, 1080, 1078, 1076, 1074, 1072, 1070, 1068, 1066, 1064)

SELECT * FROM `article` WHERE `id` IN (1090, 1088, 1086, 1084, 1082, 1080, 1078, 1076, 1074, 1072, 1070, 1068, 1066, 1064)



{"user":"289","blacklistItems":[],"num":10,"blacklist":[4737838,6046746,6244222,6244508,6244058,6244250,1582830,6244322,6244432,6244544,10154666,10188058,10428602,10390276,10339794,9313678,7672980,10318382,10479892,10387808,10543904,10548912,10551138,10480506,10552292,10553338,10508542,10543850,10553644,10553374,10553904,10555936,10558816,10558290,10559332,10554358,10555818,10559222,10556044,10554558,10560720,10562048,10565824,10563762,10564754,10567942,10561882,10565754,10565818,10567078,10576608,10579008,10580306,10584758,10583016,10584570,10583436,10583820,10583310,10583528,10586592,10585954,10585540,10586086,10585804,10586668,10585550,10585662,10587054,10585226,10587234,10587286,10587176,10587288,10587528,10587704,10587178,10587100,10587756,10587590],"type":"all","language":"en"}, Result = "Result is ignored"


select distinct(product_id) from article_product where product_id is not NULL limit 10;



select distinct(product_id) from article_product where product_id is not NULL  and article_id in (1066, 1088) and product_id not in (1582830, 4737838) limit 10;


select article_id, count(resource_url) as count_res from article_resource where article_id in (300, 302, 304, 306, 308) limit 1;

select article_id, count(resource_url) as count_res from article_resource where article_id in (300, 302, 304, 306, 308) and count_res > 3 group by article_id;

select article_id, resource_url from article_resource where article_id=300 limit 3;

select article_id, resource_url from (select article_id as a_id, resource_url from article_resource where article_id=300 limit 3) where article_id in ;

SELECT DISTINCT b.user_name,b.town_name FROM (SELECT DISTINCT farmer_id FROM t_farmers_images WHERE create_time>='2017-08-18') a
LEFT JOIN t_farmers b ON a.farmer_id=b.id 

CriteriaBuilder builder = em.getCriteriaBuilder();
CriteriaQuery<Tickets> query = builder.createQuery(Tickets.class);
EntityType<Tickets> type = em.getMetamodel().entity(Tickets.class);
EntityType<TicketsUpdates> typeTU = em.getMetamodel().entity(TicketsUpdates.class);
Root<Tickets> root = query.from(Tickets.class);
Root<TicketsUpdates> rootTicketsUpdates = query.from(TicketsUpdates.class);

Join<Tickets,TicketsUpdates> tupdates = rootTicketsUpdates.join("tickets");


public List<ArticleProduct> queryTest(Set<Integer> articleIds, List<Integer> blacklist, Integer num){
    List<ArticleProduct> articleProductsRelationship = null;
    Map<Integer, List<Integer>> articleProducts = new HashMap();
    List<Integer> productIds = new ArrayList();
//        List<Integer> productIdsInArticle = queryDistinctProductIdsInArticles(articleIds, blacklist, num);
//        if(collectionUtils.isAvailable(productIdsInArticle)){
    Session session = hibernateUtil.getSessionFrontendJinbagFactory().openSession();
    CriteriaBuilder criteriaBuilder = session.getCriteriaBuilder();
    CriteriaQuery<ArticleProduct> majorQuer = criteriaBuilder.createQuery(ArticleProduct.class);
    Root root = majorQuer.from(ArticleProduct.class);

    // subquery
    Subquery<Integer> subquery = majorQuer.subquery(Integer.class);
    Root<ArticleProduct> subroot = subquery.from(ArticleProduct.class);
//        subquery.alias("subquery");
//        Join<ArticleProduct, ArticleProduct> join = subroot.join("productId", JoinType.LEFT);
    subquery.select(subroot.get("productId"));
    subquery.distinct(true);
    Path<List<Integer>> path = subroot.get("productId");
    CriteriaBuilder.In<List<Integer>> in = criteriaBuilder.in(path);
    in.value(blacklist);

//        Predicate predicate = criteriaBuilder.equal(subroot.get("productId"), root);
    subquery.where(criteriaBuilder.and(criteriaBuilder.isNotNull(subroot.get("productId")), criteriaBuilder.not(in)));
    majorQuer.where(criteriaBuilder.equal(root.get("productId"), subroot.get("productId")));

    articleProductsRelationship = session.createQuery(majorQuer).setMaxResults(num).getResultList();
    session.close();

//        }

//        if(collectionUtils.isAvailable(articleProductsRelationship)){
//            for(ArticleProduct articleProduct : articleProductsRelationship){
//                if(articleProducts.containsKey(articleProduct.getArticleId())){
//                    articleProducts.get(articleProduct.getArticleId()).add(articleProduct.getProductId());
//                }else{
//                    List<Integer> productIds = new ArrayList();
//                    productIds.add(articleProduct.getProductId());
//                    articleProducts.put(articleProduct.getArticleId(), productIds);
//                }
//            }
//        }

    return articleProductsRelationship;
}



    public Map<Integer, List<Integer>> queryTest(Set<Integer> articleIds, List<Integer> blacklist, Integer num){
        List<ArticleProduct> articleProductsRelationship = null;
        Map<Integer, List<Integer>> articleProducts = new HashMap();
        List<Integer> productIdsInArticle = queryDistinctProductIdsInArticles(articleIds, blacklist, num);
        if(collectionUtils.isAvailable(productIdsInArticle)){
            Session session = hibernateUtil.getSessionFrontendJinbagFactory().openSession();
            CriteriaBuilder criteriaBuilder = session.getCriteriaBuilder();
            CriteriaQuery<ArticleProduct> criteriaQuery = criteriaBuilder.createQuery(ArticleProduct.class);
            Root<ArticleProduct> root = criteriaQuery.from(ArticleProduct.class);
            Join<ArticleProduct, ArticleProduct> joinArticleProduct = root.join("productId");
            criteriaQuery.where(criteriaBuilder.)


            criteriaQuery.select(root);

            try{
                session.getTransaction().begin();
                articleProductsRelationship = (List<ArticleProduct>)session.createQuery(
                        "select ap from  and ap.status=0")
                            .setParameter("productIds", productIdsInArticle)
                            .list();
                session.getTransaction().commit();
            }catch (HibernateException he){
                logger.error(he.getMessage());
            }finally {
                session.close();
            }

        }

        if(collectionUtils.isAvailable(articleProductsRelationship)){
            for(ArticleProduct articleProduct : articleProductsRelationship){
                if(articleProducts.containsKey(articleProduct.getArticleId())){
                    articleProducts.get(articleProduct.getArticleId()).add(articleProduct.getProductId());
                }else{
                    List<Integer> productIds = new ArrayList();
                    productIds.add(articleProduct.getProductId());
                    articleProducts.put(articleProduct.getArticleId(), productIds);
                }
            }
        }

        return articleProducts;
    }


10672022,10672148,10672270,10672978,10673410 |
|   10673628 |
|   10674126 |
|   10674574 |
|   10674656 |
|   10674704 |
|   10674818 |
|   10674858 |
|   10674932 |
|   10675002 |


10851766


select distinct(ap.product_id) from article_product ap where ap.product_id not in (10672022,10672148,10672270,10672978,10673410) and article_id in (1090, 1088, 1086, 1084) and status=0 limit 10;

select distinct(ap.product_id) as dic_product_id from article_product ap where product_id not in (10672022,10672148,10672270,10672978,10673410) and article_id in (1090, 1088, 1086, 1084) and status=0 limit 10;

select article_id, product_id from article_product as app inner join (select distinct(ap.product_id) as dic_product_id from article_product ap where product_id not in (10672022,10672148,10672270,10672978,10673410) and article_id in (1090, 1088, 1086, 1084) and status=0 limit 10) as dic on (app.product_id=dic.dic_product_id) where app.article_id in (1090, 1088, 1086, 1084);

select article_id, product_id from article_product as app where app.product_id in (select distinct(ap.product_id) as dic_product_id from article_product ap where product_id not in (10672022,10672148,10672270,10672978,10673410) and article_id in (1090, 1088, 1086, 1084) and status=0) and app.article_id in (1090, 1088, 1086, 1084);


// create the outer query
CriteriaBuilder cb = em.getCriteriaBuilder();
CriteriaQuery cq = cb.createQuery(Author.class);
Root root = cq.from(Author.class);
 
// count books written by an author
Subquery sub = cq.subquery(Long.class);
Root subRoot = sub.from(Book.class);
SetJoin<Book, Author> subAuthors = subRoot.join(Book_.authors);
sub.select(cb.count(subRoot.get(Book_.id)));
sub.where(cb.equal(root.get(Author_.id), subAuthors.get(Author_.id)));
 
// check the result of the subquery
cq.where(cb.greaterThanOrEqualTo(sub, 3L));
 
TypedQuery query = em.createQuery(cq);
List authors = query.getResultList();



select major.article_id as major_article_id, major.product_id as major_product_id from article_product as major left join article_product as sub on sub.product_id=major.product_id;


10851766