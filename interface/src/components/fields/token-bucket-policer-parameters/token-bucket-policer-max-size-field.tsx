import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TokenBucketPolicerParameterFieldProps } from './token-bucket-policer-parameters';

export function TokenBucketPolicerMaxSizeField(props: TokenBucketPolicerParameterFieldProps): ReactElement {
  const { tokenBucketPolicerParameters, setTokenBucketPolicerParameters } = props;

  const tokenBucketPolicerMaxSize = useMemo(() => {
    return tokenBucketPolicerParameters.bucket_max_size || '';
  }, [tokenBucketPolicerParameters]);

  const setTokenBucketPolicerMaxSize = useSetNfvTeFunctionParameter('bucket_max_size', setTokenBucketPolicerParameters);
  const onTokenBucketPolicerMaxSizeChangeHandler = useChangeHandler(setTokenBucketPolicerMaxSize);

  return (
    <FormInput
      label="Tamanho Máximo do Bucket"
      name="bucket-max-size"
      value={tokenBucketPolicerMaxSize}
      placeholder="Valor em tokens"
      onChange={onTokenBucketPolicerMaxSizeChangeHandler}
    />
  );
}
