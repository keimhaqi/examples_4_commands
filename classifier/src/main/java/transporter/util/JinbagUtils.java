package transporter.util;

import transporter.util.json.JsonMapper;
import org.springframework.context.annotation.Configuration;

@Configuration
public class JinbagUtils {
    private JsonMapper jsonMapper = null;
    private JsonMapper nullJsonMapper = null;

    private static JsonMapper staticJsonMapper = null;

    public JinbagUtils(){
        if(jsonMapper == null){
            jsonMapper = JsonMapper.nonNullMapper();
        }

        if(nullJsonMapper == null){
            nullJsonMapper = JsonMapper.nonDefaultMapper();
        }
    }

    // retrieve only numbers from string
    public static Float getNumberOnly(String sprice){
        if(isEmpty(sprice)) return null;
        char [] price = sprice.toCharArray();
        String ret = "";
        Float value = null;
        for(char letter : price){
            if(letter >= 48 && letter <= 57 || letter == 46){
                ret += letter;
            }
        }
        try{
            value = Float.parseFloat(ret);
            return value;
        }catch (NumberFormatException nfe){
            return 0.0f;
        }
    }

    public static JsonMapper jsonMapperInstance(){
        if(staticJsonMapper == null){
            staticJsonMapper = JsonMapper.nonNullMapper();
        }
        return staticJsonMapper;
    }

    public JsonMapper getJsonMapper() {
        return jsonMapper;
    }

    public void setJsonMapper(JsonMapper jsonMapper) {
        this.jsonMapper = jsonMapper;
    }

    public JsonMapper getNullJsonMapper() {
        return nullJsonMapper;
    }

    public void setNullJsonMapper(JsonMapper nullJsonMapper) {
        this.nullJsonMapper = nullJsonMapper;
    }

    public static boolean isEmpty(String string){
        return (string == null || "".equals(string.trim()));
    }
}
