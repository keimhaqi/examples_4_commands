package transporter.data.sql.daoService.frontend.jinbag.serviceimpl;

import transporter.Application;
import transporter.data.sql.daoService.frontend.jinbag.services.ISemiProductService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.ApplicationContext;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.web.WebAppConfiguration;

@RunWith(SpringRunner.class)
@SpringBootTest(classes = Application.class)
@WebAppConfiguration
public class SemiProductServiceImplTest {

    @Autowired
    private ApplicationContext ctx;
    @Test
    public void queryById() {
        ISemiProductService semiProductService = ctx.getAutowireCapableBeanFactory()
                .createBean(SemiProductServiceImpl.class);
        semiProductService.queryById(1l);
    }
}