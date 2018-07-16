package transporter.core.services;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import transporter.core.services.rule.service.IRuleService;
import transporter.core.services.rule.service.RuleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;

@Configuration
public class Service {

    private static Logger logger = LoggerFactory.getLogger(Service.class);

    private final IRuleService ruleService;

    @Autowired
    public Service(RuleService ruleService) {
        this.ruleService = ruleService;
    }

    public boolean transport4HotProduct(String message){
        System.out.println(message);
        ruleService.classifier(message);
        return false;
    }
}
