import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { TokenBucketShaperParameterFieldProps } from './token-bucket-shaper-parameters';

export function TokenBucketShaperBucketSizeField(props: TokenBucketShaperParameterFieldProps): ReactElement {
  const { tokenBucketShaperParameters, setTokenBucketShaperParameters } = props;

  const tokenBucketShaperBucketSize = useMemo(() => {
    return tokenBucketShaperParameters.bucket_size || '';
  }, [tokenBucketShaperParameters]);

  const setTokenBucketShaperBucketSize = useSetNfvTeFunctionParameter('bucket_size', setTokenBucketShaperParameters);
  const onTokenBucketShaperBucketSizeChangeHandler = useChangeHandler(setTokenBucketShaperBucketSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket"
      name="bucket-size"
      value={tokenBucketShaperBucketSize}
      onChange={onTokenBucketShaperBucketSizeChangeHandler}
    />
  );
}
